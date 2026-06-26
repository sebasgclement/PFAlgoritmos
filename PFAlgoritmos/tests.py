"""
╔══════════════════════════════════════════════════════════╗
║  TESTS — Cajero CapacitarTec 4.0                        ║
║                                                          ║
║  Cómo usar:                                              ║
║    python tests.py                                       ║
║                                                          ║
║  Antes de hacer push, asegurense de que todos los        ║
║  tests de SU grupo estén en verde ✅                     ║
╚══════════════════════════════════════════════════════════╝
"""

from cajero import verificar_pin, consultar_saldo, retirar, depositar, generar_resumen

# ── Utilidad para mostrar resultados ────────────────────────
errores = []

def test(grupo, descripcion, obtenido, esperado):
    if obtenido == esperado:
        print(f"  ✅  {descripcion}")
    else:
        print(f"  ❌  {descripcion}")
        print(f"       esperado : {repr(esperado)}")
        print(f"       obtenido : {repr(obtenido)}")
        errores.append(grupo)

def seccion(titulo, color=""):
    colores = {"g1":"\033[91m","g2":"\033[96m","g3":"\033[94m","g4":"\033[92m","g5":"\033[95m","":"\033[0m"}
    fin = "\033[0m"
    print(f"\n{colores.get(color,'')}{titulo}{fin}")
    print("─" * 50)


# ══════════════════════════════════════════════════════════
#  GRUPO 1 — verificar_pin
# ══════════════════════════════════════════════════════════
seccion("GRUPO 1 — verificar_pin()", "g1")

res = verificar_pin(1234, 1)
if res is None:
    print("  ⚠️  Función no implementada todavía.")
else:
    # PIN correcto al primer intento → acceso True, no bloqueado
    test("G1", "PIN correcto → acceso = True",   res[0], True)
    test("G1", "PIN correcto → bloqueado = False", res[2], False)

res = verificar_pin(9999, 1)
if res is None:
    print("  ⚠️  Función no implementada todavía.")
else:
    # PIN incorrecto intento 1 → no accede, no bloquea, mensaje incluye "2"
    test("G1", "PIN incorrecto intento 1 → acceso = False",   res[0], False)
    test("G1", "PIN incorrecto intento 1 → bloqueado = False", res[2], False)
    test("G1", "PIN incorrecto intento 1 → mensaje menciona intentos restantes",
         "2" in res[1] or "dos" in res[1].lower(), True)

res = verificar_pin(9999, 3)
if res is None:
    print("  ⚠️  Función no implementada todavía.")
else:
    # 3 intentos fallidos → bloqueado
    test("G1", "3 intentos fallidos → acceso = False",   res[0], False)
    test("G1", "3 intentos fallidos → bloqueado = True",  res[2], True)


# ══════════════════════════════════════════════════════════
#  GRUPO 2 — consultar_saldo
# ══════════════════════════════════════════════════════════
seccion("GRUPO 2 — consultar_saldo()", "g2")

res = consultar_saldo(50000.0)
if res is None:
    print("  ⚠️  Función no implementada todavía.")
else:
    test("G2", "50000.0  → '$ 50.000,00'", res, "$ 50.000,00")

res = consultar_saldo(1234.5)
if res is None:
    print("  ⚠️  Función no implementada todavía.")
else:
    test("G2", "1234.5   → '$ 1.234,50'",  res, "$ 1.234,50")

res = consultar_saldo(0.0)
if res is None:
    print("  ⚠️  Función no implementada todavía.")
else:
    test("G2", "0.0      → '$ 0,00'",       res, "$ 0,00")


# ══════════════════════════════════════════════════════════
#  GRUPO 3 — retirar
# ══════════════════════════════════════════════════════════
seccion("GRUPO 3 — retirar()", "g3")

res = retirar(50000, 10000)
if res is None:
    print("  ⚠️  Función no implementada todavía.")
else:
    # 10000 + comisión 0.5% (50) = 10050 descontados → saldo 39950
    test("G3", "Retiro válido → nuevo saldo = 39950.0", res[0], 39950.0)
    test("G3", "Retiro válido → exito = True",           res[2], True)

res = retirar(50000, 60000)
if res is None:
    print("  ⚠️  Función no implementada todavía.")
else:
    # Fondos insuficientes → saldo sin cambio
    test("G3", "Fondos insuficientes → saldo sin cambio", res[0], 50000)
    test("G3", "Fondos insuficientes → exito = False",    res[2], False)

res = retirar(50000, 0)
if res is None:
    print("  ⚠️  Función no implementada todavía.")
else:
    test("G3", "Monto 0  → exito = False", res[2], False)

res = retirar(50000, -500)
if res is None:
    print("  ⚠️  Función no implementada todavía.")
else:
    test("G3", "Monto negativo → exito = False", res[2], False)


# ══════════════════════════════════════════════════════════
#  GRUPO 4 — depositar
# ══════════════════════════════════════════════════════════
seccion("GRUPO 4 — depositar()", "g4")

res = depositar(50000, 5000)
if res is None:
    print("  ⚠️  Función no implementada todavía.")
else:
    test("G4", "Depósito válido → nuevo saldo = 55000.0", res[0], 55000.0)
    test("G4", "Depósito válido → exito = True",           res[2], True)

res = depositar(50000, 0)
if res is None:
    print("  ⚠️  Función no implementada todavía.")
else:
    test("G4", "Monto 0  → saldo sin cambio", res[0], 50000)
    test("G4", "Monto 0  → exito = False",     res[2], False)

res = depositar(50000, -100)
if res is None:
    print("  ⚠️  Función no implementada todavía.")
else:
    test("G4", "Monto negativo → exito = False", res[2], False)


# ══════════════════════════════════════════════════════════
#  GRUPO 5 — generar_resumen
# ══════════════════════════════════════════════════════════
seccion("GRUPO 5 — generar_resumen()", "g5")

res = generar_resumen(2, 1, 15000.0, 5000.0, 60000.0)
if res is None:
    print("  ⚠️  Función no implementada todavía.")
else:
    test("G5", "Retorna un string",              isinstance(res, str),  True)
    test("G5", "Menciona cantidad de depósitos", "2" in res,            True)
    test("G5", "Menciona cantidad de retiros",   "1" in res,            True)
    test("G5", "Menciona el saldo final",        "60" in res,           True)

res_vacio = generar_resumen(0, 0, 0.0, 0.0, 50000.0)
if res_vacio is None:
    print("  ⚠️  Función no implementada todavía.")
else:
    test("G5", "Sesión sin operaciones → sigue siendo string", isinstance(res_vacio, str), True)


# ══════════════════════════════════════════════════════════
#  RESUMEN FINAL
# ══════════════════════════════════════════════════════════
print("\n" + "═" * 50)
if not errores:
    print("  🎉  ¡Todos los tests pasaron! Listo para el push.")
else:
    grupos_fallidos = sorted(set(errores))
    print(f"  ⚠️  Hay tests fallando en: {', '.join(grupos_fallidos)}")
    print("     Revisen los casos marcados con ❌ antes de hacer push.")
print("═" * 50 + "\n")
