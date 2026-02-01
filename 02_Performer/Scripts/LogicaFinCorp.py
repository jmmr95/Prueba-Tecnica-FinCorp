import json
import re
from datetime import datetime, timedelta

def procesar_datos(in_Monto, in_Fecha, in_Concepto):
    try:
        # --------------------------
        # --- 1. LIMPIEZA MONTO ---
        # --------------------------

        if not in_Monto:
            in_Monto = "0"
            
        limpio = re.sub(r'[^\d,.-]', '', str(in_Monto))
        monto_final = 0.0

        try:
            if '.' in limpio and ',' in limpio:
                if limpio.find('.') < limpio.find(','):
                    limpio = limpio.replace('.', '').replace(',', '.')
                else:
                    limpio = limpio.replace(',', '')
            elif ',' in limpio:
                partes = limpio.split(',')
                if len(partes[-1]) == 2:
                    limpio = limpio.replace(',', '.')
                else:
                    limpio = limpio.replace(',', '')
            elif '.' in limpio:
                partes = limpio.split('.')
                if len(partes[-1]) == 3:
                    limpio = limpio.replace('.', '')

            monto_final = float(limpio)
        except:
            monto_final = 0.0

        # --------------------------------------
        # --- 2. FECHA + FRAUD CHECK (SIN HORA) ---
        # --------------------------------------

        estado = "OK"
        fecha_norm = ""

        try:
            if isinstance(in_Fecha, datetime):
                fecha_obj = in_Fecha.date()

            else:
                f = str(in_Fecha)

                # limpieza UiPath / Excel
                f = f.replace('[','').replace(']','')
                f = f.replace('\xa0','').replace('\r','').replace('\n','').strip()

                # quitar hora si existe
                if " " in f:
                    f = f.split(" ")[0]

                # serial excel
                if f.isdigit():
                    fecha_obj = (datetime(1899, 12, 30) + timedelta(days=int(f))).date()

                else:
                    # MM/DD/YYYY (Orchestrator)
                    try:
                        fecha_obj = datetime.strptime(f, "%m/%d/%Y").date()
                    except:
                        # DD/MM/YYYY
                        fecha_obj = datetime.strptime(f, "%d/%m/%Y").date()

            fecha_norm = fecha_obj.strftime("%Y-%m-%d")

            # weekday(): lunes=0 ... domingo=6
            review_required = fecha_obj.weekday() >= 5

            estado = "REVIEW" if review_required else "OK"

        except:
            estado = "REVIEW"
            fecha_norm = str(in_Fecha)
            review_required = True

        # -------------------------------
        # --- 3. IVA CONDICIONAL ---
        # -------------------------------

        impuesto = 0.0
        concepto_lower = str(in_Concepto).lower()

        if "software" in concepto_lower or "licencia" in concepto_lower:
            impuesto = 0.0
        else:
            impuesto = round(monto_final * 0.19, 2)

        # --------------------
        # --- 4. SALIDA ---
        # --------------------

        resultado = {
            "finalAmount": monto_final,
            "taxApplied": impuesto,
            "status": estado,
            "normalizedDate": fecha_norm
        }

        return json.dumps(resultado)

    except Exception as e:
        return json.dumps({
            "finalAmount": 0.0,
            "taxApplied": 0.0,
            "status": "ERROR",
            "normalizedDate": str(e)
        })

