# 🏦 Cajero Automático — CapacitarTec 4.0

Proyecto integrador de Python. Cada grupo implementa **una función**. Cuando todas se juntan, el cajero funciona completo.

---

## 🚀 Cómo arrancar

```bash
# 1. Clonar el repositorio
git clone <URL-del-repo>
cd cajero-capacitar

# 2. Crear la rama de tu grupo (reemplazar X y el nombre)
git checkout -b grupo-1/verificar-pin

# 3. Abrir cajero.py y buscar tu sección con # ← GRUPO X
# 4. Implementar la función
# 5. Verificar con los tests
python tests.py

# 6. Commitear y subir cuando esté listo
git add cajero.py
git commit -m "feat: implementa verificar_pin"
git push origin grupo-1/verificar-pin
```

---

## 👥 Grupos y funciones

| Grupo | Rama | Función | Retorna |
|-------|------|---------|---------|
| G1 | `grupo-1/verificar-pin` | `verificar_pin(pin, intentos)` | `(acceso, mensaje, bloqueado)` |
| G2 | `grupo-2/consultar-saldo` | `consultar_saldo(saldo)` | `str` |
| G3 | `grupo-3/retirar` | `retirar(saldo, monto)` | `(nuevo_saldo, mensaje, exito)` |
| G4 | `grupo-4/depositar` | `depositar(saldo, monto)` | `(nuevo_saldo, mensaje, exito)` |
| G5 | `grupo-5/resumen-sesion` | `generar_resumen(n_dep, n_ret, total_dep, total_ret, saldo)` | `str` |

---

## 🧪 Cómo probar sin el otro grupo

El cajero funciona aunque las demás funciones no estén implementadas. Si una función devuelve `None`, la interfaz lo avisa en amarillo y sigue andando.

Para probar **solo tu función**:
```bash
python tests.py
```

Para probar **la interfaz completa**:
```bash
python cajero.py
```

PIN de prueba: `1234` · Saldo inicial: `$50.000`

---

## ✅ Checklist antes del push

- [ ] Mi función **no** devuelve `None`
- [ ] `python tests.py` muestra ✅ en todos los tests de mi grupo
- [ ] Probé los casos extremos (monto 0, monto negativo, saldo exacto)
- [ ] El mensaje que devuelvo tiene sentido para el usuario

---

## 📁 Estructura del proyecto

```
cajero-capacitar/
├── cajero.py   ← archivo principal (GUI + funciones)
├── tests.py    ← tests para verificar tu función
└── README.md   ← este archivo
```
