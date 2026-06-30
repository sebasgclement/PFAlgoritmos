"""
╔══════════════════════════════════════════════════════════════╗
║         CAJERO AUTOMÁTICO — CapacitarTec 4.0                 ║
║         Python + Tkinter                                     ║
╠══════════════════════════════════════════════════════════════╣
║  INSTRUCCIONES PARA LOS GRUPOS:                              ║
║                                                              ║
║  Busquen el comentario  # ← GRUPO X                         ║
║  Implementen su función SIN modificar nada más.              ║
║  Para probar: corran el archivo y usen la interfaz.          ║
║                                                              ║
║  PIN de prueba: 1234   |   Saldo inicial: $50.000            ║
╚══════════════════════════════════════════════════════════════╝
"""

import tkinter as tk
from tkinter import font as tkf

# ── CONFIGURACIÓN DEL BANCO ─────────────────────────────────
PIN_CORRECTO    = 1234
SALDO_INICIAL   = 50_000.0
MAX_INTENTOS    = 3
MAX_OPERACIONES = 5
COMISION        = 0.005   # 0.5% sobre cada retiro

# ── PALETA DE COLORES ────────────────────────────────────────
C_BG      = "#0D1B2A"
C_SCREEN  = "#0A2540"
C_CARD    = "#112A45"
C_TEAL    = "#00D4C8"
C_YELLOW  = "#F5C842"
C_GREEN   = "#2ED573"
C_RED     = "#FF4757"
C_TEXT    = "#E8F0FE"
C_DIM     = "#5A7090"
C_BTN     = "#1A3A5C"
C_BTN_H   = "#224D7A"


# ════════════════════════════════════════════════════════════
#  ZONA DE TRABAJO — Cada grupo implementa su función aquí
# ════════════════════════════════════════════════════════════

def verificar_pin(pin_ingresado, intentos_usados):
    """
    GRUPO 1 — Verificación de PIN
    ──────────────────────────────
    Verifica si el PIN ingresado es correcto y decide si el
    acceso se concede o si la tarjeta queda bloqueada.

    Parámetros:
        pin_ingresado  (int): el PIN que escribió el usuario
        intentos_usados (int): cuántos intentos lleva (incluye este)

    Retorna una tupla con tres valores: (acceso, mensaje, bloqueado)
        acceso    (bool): True si el PIN es correcto
        mensaje   (str) : texto que se muestra en pantalla
        bloqueado (bool): True si se agotaron los MAX_INTENTOS

    Ejemplos esperados:
        verificar_pin(1234, 1) → (True,  "✓ Acceso concedido. Bienvenido/a.", False)
        verificar_pin(9999, 1) → (False, "PIN incorrecto. Te quedan 2 intentos.", False)
        verificar_pin(9999, 2) → (False, "PIN incorrecto. Te queda 1 intento.", False)
        verificar_pin(9999, 3) → (False, "✗ Tarjeta bloqueada por seguridad.", True)
    """
    pass  # ← GRUPO 1: reemplazar este pass con el código


def consultar_saldo(saldo):
    """
    GRUPO 2 — Formateo de saldo
    ────────────────────────────
    Recibe el saldo como número y lo devuelve como string
    formateado con signo $, punto como separador de miles
    y coma para decimales.

    Parámetros:
        saldo (float): el saldo actual

    Retorna:
        str: saldo formateado

    Ejemplos esperados:
        consultar_saldo(50000.0) → "$ 50.000,00"
        consultar_saldo(1234.5)  → "$ 1.234,50"
        consultar_saldo(0.0)     → "$ 0,00"

    Pista: investigar f-strings con formato numérico, o
           usar el método str.replace() para adaptar el formato.
    """
    pass  # ← GRUPO 2: reemplazar este pass con el código


def retirar(saldo, monto):
    """
    GRUPO 3 — Retiro de dinero
    ───────────────────────────
    Valida el monto y procesa el retiro descontando también
    la comisión del 0.5%.

    Parámetros:
        saldo (float): saldo actual antes del retiro
        monto (float): monto que el usuario quiere retirar

    Retorna una tupla: (nuevo_saldo, mensaje, exito)
        nuevo_saldo (float): saldo después de la operación
        mensaje     (str)  : texto que se muestra en pantalla
        exito       (bool) : True si la operación fue válida

    Reglas de validación (en orden):
        1. El monto debe ser mayor a 0
        2. El total a descontar es: monto + (monto * COMISION)
        3. El total a descontar no puede superar el saldo

    Ejemplos esperados:
        retirar(50000, 10000) → (39950.0, "✓ Retiro de $10.000,00 OK. Comisión: $50,00", True)
        retirar(50000, 60000) → (50000,   "✗ Fondos insuficientes.", False)
        retirar(50000, -500)  → (50000,   "✗ El monto debe ser mayor a 0.", False)
        retirar(50000, 0)     → (50000,   "✗ El monto debe ser mayor a 0.", False)
    """
    pass  # ← GRUPO 3: reemplazar este pass con el código


def depositar(saldo, monto):
    """
    GRUPO 4 — Depósito de dinero
    ─────────────────────────────
    def depositar(saldo , monto):
      if monto >0: 
       nuevo_saldo = saldo + monto 
       mensaje = "Depósito realizado con éxito".
       exito = True
      else: 
       nuevo_saldo = saldo
       mensaje = "Error: El monto a depositar debe ser mayor a cero".
       exito = False 
      return nuevo_saldo,mensaje,exito
    """
    


def generar_resumen(n_dep, n_ret, total_dep, total_ret, saldo_final):
    """
    GRUPO 5 — Resumen de sesión
    ────────────────────────────
    Genera el texto completo del resumen al cerrar la sesión.

    Parámetros:
        n_dep       (int)  : cantidad de depósitos realizados
        n_ret       (int)  : cantidad de retiros realizados
        total_dep   (float): suma total de todos los depósitos
        total_ret   (float): suma total de todos los retiros (sin comisión)
        saldo_final (float): saldo al momento de cerrar sesión

    Retorna:
        str: el texto completo del resumen (usar \\n para saltos de línea)

    Ejemplo de salida esperada:
        ════ RESUMEN DE SESIÓN ════
        Depósitos : 2  ($ 15.000,00)
        Retiros   : 1  ($  5.000,00)
        ──────────────────────────
        Saldo final: $ 60.000,00
        ¡Hasta pronto!

    Pista: construir el string línea a línea con \\n entre cada una.
    """
    pass  # ← GRUPO 5: reemplazar este pass con el código


# ════════════════════════════════════════════════════════════
#  GUI — NO MODIFICAR A PARTIR DE AQUÍ
#  (la interfaz gráfica ya está implementada y llama a
#   sus funciones automáticamente)
# ════════════════════════════════════════════════════════════

class CajeroApp:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Banco CapacitarTec 4.0")
        self.root.geometry("400x660")
        self.root.resizable(False, False)
        self.root.configure(bg=C_BG)

        # Estado de la sesión
        self.saldo       = SALDO_INICIAL
        self.intentos    = 0
        self.pin_buf     = ""
        self.monto_buf   = ""
        self.modo        = ""        # "depositar" | "retirar"
        self.n_dep       = 0
        self.n_ret       = 0
        self.total_dep   = 0.0
        self.total_ret   = 0.0
        self.operaciones = 0
        self._screen     = ""

        # Tipografías
        self.f_title = tkf.Font(family="Helvetica", size=13, weight="bold")
        self.f_big   = tkf.Font(family="Courier",   size=26, weight="bold")
        self.f_med   = tkf.Font(family="Courier",   size=13)
        self.f_btn   = tkf.Font(family="Helvetica", size=11, weight="bold")
        self.f_sm    = tkf.Font(family="Helvetica", size=9)
        self.f_mono  = tkf.Font(family="Courier",   size=10)

        self._build_ui()
        self._show_pin()

    # ── CONSTRUCCIÓN DE LA UI ─────────────────────────────────

    def _build_ui(self):
        # Cabecera del banco
        hdr = tk.Frame(self.root, bg="#06111F", pady=10)
        hdr.pack(fill="x")
        tk.Label(hdr, text="🏦  BANCO CAPACITAR 4.0",
                 font=self.f_title, bg="#06111F", fg=C_TEAL).pack()

        # Barra de estado
        self._status_frame = tk.Frame(self.root, bg=C_CARD, height=28)
        self._status_frame.pack(fill="x")
        self._status_var = tk.StringVar(value="Bienvenido/a")
        self._ops_var    = tk.StringVar(value="")
        tk.Label(self._status_frame, textvariable=self._status_var,
                 font=self.f_sm, bg=C_CARD, fg=C_DIM).pack(side="left",  padx=10)
        tk.Label(self._status_frame, textvariable=self._ops_var,
                 font=self.f_sm, bg=C_CARD, fg=C_YELLOW).pack(side="right", padx=10)

        # Pantalla principal
        self._scr = tk.Frame(self.root, bg=C_SCREEN, height=230,
                             relief="sunken", bd=2)
        self._scr.pack(fill="x", padx=12, pady=8)
        self._scr.pack_propagate(False)

        # Teclado numérico
        kp = tk.Frame(self.root, bg=C_BG)
        kp.pack(pady=2)
        layout = [["7","8","9"], ["4","5","6"], ["1","2","3"], ["⌫","0","✓"]]
        for r, row in enumerate(layout):
            for c, k in enumerate(row):
                bg = C_TEAL if k=="✓" else (C_RED if k=="⌫" else C_BTN)
                fg = C_BG   if k=="✓" else C_TEXT
                tk.Button(kp, text=k, width=5, height=2, font=self.f_btn,
                          bg=bg, fg=fg, activebackground=C_BTN_H,
                          activeforeground=C_TEXT, relief="flat", bd=0,
                          cursor="hand2",
                          command=lambda key=k: self._key(key)
                          ).grid(row=r, column=c, padx=4, pady=3)

        # Botones de acción
        af = tk.Frame(self.root, bg=C_BG)
        af.pack(fill="x", padx=12, pady=6)
        self._btn_cancel = tk.Button(af, text="✕  CANCELAR",
                                     font=self.f_btn, bg="#3A1A1A", fg=C_RED,
                                     activebackground="#5A2222", relief="flat",
                                     bd=0, cursor="hand2", width=14,
                                     command=self._cancel)
        self._btn_cancel.pack(side="left", padx=4)
        self._btn_menu = tk.Button(af, text="☰  MENÚ",
                                   font=self.f_btn, bg=C_BTN, fg=C_TEXT,
                                   activebackground=C_BTN_H, relief="flat",
                                   bd=0, cursor="hand2", width=14,
                                   command=self._show_menu)
        # btn_menu aparece solo después del login

    # ── PANTALLAS ─────────────────────────────────────────────

    def _clear(self):
        for w in self._scr.winfo_children():
            w.destroy()

    def _show_pin(self):
        self._clear()
        self._screen  = "pin"
        self.pin_buf  = ""
        self.intentos = 0
        self._btn_menu.pack_forget()
        self._status_var.set("Por favor ingrese su PIN")
        self._ops_var.set("")

        tk.Label(self._scr, text="INGRESE SU PIN",
                 font=self.f_title, bg=C_SCREEN, fg=C_DIM).pack(pady=(20,8))
        self._pin_dots = tk.Label(self._scr, text="○  ○  ○  ○",
                                  font=self.f_big, bg=C_SCREEN, fg=C_YELLOW)
        self._pin_dots.pack(pady=8)
        self._pin_msg = tk.Label(self._scr, text="",
                                 font=self.f_sm, bg=C_SCREEN, fg=C_DIM,
                                 wraplength=340)
        self._pin_msg.pack(pady=4)

    def _refresh_pin_dots(self):
        n = len(self.pin_buf)
        self._pin_dots.config(text="  ".join(["●"]*n + ["○"]*(4-n)))

    def _show_menu(self):
        self._clear()
        self._screen = "menu"
        self._btn_menu.pack_forget()
        self._status_var.set("Sesión activa")
        self._ops_var.set(f"Ops: {self.operaciones}/{MAX_OPERACIONES}")

        # Saldo formateado (llama a la función del Grupo 2)
        saldo_fmt = consultar_saldo(self.saldo)
        if saldo_fmt is None:
            saldo_fmt = f"${self.saldo:,.2f}  ⚠ Grupo 2 pendiente"

        tk.Label(self._scr, text="SALDO DISPONIBLE",
                 font=self.f_sm, bg=C_SCREEN, fg=C_DIM).pack(pady=(14,0))
        tk.Label(self._scr, text=saldo_fmt,
                 font=self.f_big, bg=C_SCREEN, fg=C_GREEN).pack(pady=6)

        ops = [
            ("💳  Depositar",     "#1A3A2A", C_GREEN,  self._start_dep),
            ("💸  Retirar",       "#3A1A1A", C_RED,    self._start_ret),
            ("📋  Ver resumen",   "#1A2A3A", C_TEAL,   self._show_resumen),
            ("🚪  Cerrar sesión", C_CARD,    C_DIM,    self._cerrar),
        ]
        for txt, bg, fg, cmd in ops:
            tk.Button(self._scr, text=txt, font=self.f_btn,
                      bg=bg, fg=fg, relief="flat", bd=0, cursor="hand2",
                      activebackground=C_BTN_H, activeforeground=C_TEXT,
                      width=30, pady=4, command=cmd).pack(fill="x", padx=14, pady=2)

    def _show_trans(self, titulo, color):
        self._clear()
        self._screen    = "trans"
        self.monto_buf  = ""
        self._btn_menu.pack(side="right", padx=4)
        tk.Label(self._scr, text=titulo,
                 font=self.f_title, bg=C_SCREEN, fg=color).pack(pady=(18,4))
        tk.Label(self._scr, text="Ingrese el monto ($):",
                 font=self.f_sm, bg=C_SCREEN, fg=C_DIM).pack()
        self._monto_lbl = tk.Label(self._scr, text="$  0",
                                   font=self.f_big, bg=C_SCREEN, fg=C_YELLOW)
        self._monto_lbl.pack(pady=8)
        self._trans_msg = tk.Label(self._scr, text="",
                                   font=self.f_sm, bg=C_SCREEN, fg=C_DIM,
                                   wraplength=340)
        self._trans_msg.pack(pady=2)

    def _refresh_monto(self):
        v = int(self.monto_buf) if self.monto_buf else 0
        self._monto_lbl.config(text=f"$  {v:,}".replace(",", "."))

    def _show_msg(self, msg, color=C_TEXT, back_ms=2200):
        self._clear()
        self._screen = "msg"
        tk.Label(self._scr, text=msg, font=self.f_med,
                 bg=C_SCREEN, fg=color, wraplength=360,
                 justify="center").pack(expand=True)
        if back_ms:
            self.root.after(back_ms, self._show_menu)

    def _show_resumen(self):
        self._clear()
        self._screen = "resumen"
        self._btn_menu.pack(side="right", padx=4)
        self._status_var.set("Resumen de sesión")

        txt = generar_resumen(self.n_dep, self.n_ret,
                              self.total_dep, self.total_ret, self.saldo)
        if txt is None:
            txt = (f"⚠ Grupo 5 pendiente\n\n"
                   f"Depósitos: {self.n_dep}   Retiros: {self.n_ret}\n"
                   f"Total dep: ${self.total_dep:,.2f}\n"
                   f"Total ret: ${self.total_ret:,.2f}\n"
                   f"Saldo: ${self.saldo:,.2f}")

        tk.Label(self._scr, text="RESUMEN DE SESIÓN",
                 font=self.f_title, bg=C_SCREEN, fg=C_TEAL).pack(pady=(14,8))
        tk.Label(self._scr, text=txt, font=self.f_mono,
                 bg=C_SCREEN, fg=C_TEXT, justify="left",
                 wraplength=360).pack(padx=14)

    def _cerrar(self):
        self._show_resumen()
        self._screen = "end"
        self._btn_menu.pack_forget()
        tk.Button(self._scr, text="🚪  Salir del sistema",
                  font=self.f_btn, bg="#3A1A1A", fg=C_RED,
                  relief="flat", bd=0, cursor="hand2",
                  command=self.root.destroy).pack(pady=10)

    # ── ACCIONES ─────────────────────────────────────────────

    def _start_dep(self):
        if self.operaciones >= MAX_OPERACIONES:
            self._show_msg("Límite de operaciones alcanzado.", C_RED)
            return
        self.modo = "dep"
        self._show_trans("DEPÓSITO", C_GREEN)

    def _start_ret(self):
        if self.operaciones >= MAX_OPERACIONES:
            self._show_msg("Límite de operaciones alcanzado.", C_RED)
            return
        self.modo = "ret"
        self._show_trans("RETIRO", C_RED)

    def _key(self, k):
        if   k == "✓": self._confirm()
        elif k == "⌫": self._back()
        else:           self._digit(k)

    def _digit(self, d):
        if self._screen == "pin" and len(self.pin_buf) < 4:
            self.pin_buf += d
            self._refresh_pin_dots()
        elif self._screen == "trans" and len(self.monto_buf) < 8:
            self.monto_buf += d
            self._refresh_monto()

    def _back(self):
        if self._screen == "pin" and self.pin_buf:
            self.pin_buf = self.pin_buf[:-1]
            self._refresh_pin_dots()
        elif self._screen == "trans" and self.monto_buf:
            self.monto_buf = self.monto_buf[:-1]
            self._refresh_monto()

    def _cancel(self):
        if self._screen in ("pin", "end"):
            return
        self._show_menu()

    def _confirm(self):
        if   self._screen == "pin":   self._proc_pin()
        elif self._screen == "trans": self._proc_trans()

    def _proc_pin(self):
        if len(self.pin_buf) != 4:
            self._pin_msg.config(text="Ingrese exactamente 4 dígitos.", fg=C_DIM)
            return
        self.intentos += 1
        res = verificar_pin(int(self.pin_buf), self.intentos)
        if res is None:
            self._pin_msg.config(
                text="⚠ Grupo 1: función aún no implementada.", fg=C_YELLOW)
            return
        acceso, mensaje, bloqueado = res
        if acceso:
            self._pin_msg.config(text=mensaje, fg=C_GREEN)
            self.root.after(900, self._show_menu)
        elif bloqueado:
            self._pin_msg.config(text=mensaje, fg=C_RED)
            self._btn_cancel.config(state="disabled")
        else:
            self.pin_buf = ""
            self._refresh_pin_dots()
            self._pin_msg.config(text=mensaje, fg=C_YELLOW)

    def _proc_trans(self):
        if not self.monto_buf:
            return
        monto = float(self.monto_buf)
        if self.modo == "dep":
            res = depositar(self.saldo, monto)
            if res is None:
                self._trans_msg.config(
                    text="⚠ Grupo 4: función aún no implementada.", fg=C_YELLOW)
                return
            nuevo_saldo, mensaje, exito = res
            if exito:
                self.saldo    = nuevo_saldo
                self.n_dep   += 1
                self.total_dep += monto
                self.operaciones += 1
                self._ops_var.set(f"Ops: {self.operaciones}/{MAX_OPERACIONES}")
                self._show_msg(mensaje, C_GREEN)
            else:
                self._trans_msg.config(text=mensaje, fg=C_RED)
                self.monto_buf = ""
                self._refresh_monto()
        elif self.modo == "ret":
            res = retirar(self.saldo, monto)
            if res is None:
                self._trans_msg.config(
                    text="⚠ Grupo 3: función aún no implementada.", fg=C_YELLOW)
                return
            nuevo_saldo, mensaje, exito = res
            if exito:
                self.saldo    = nuevo_saldo
                self.n_ret   += 1
                self.total_ret += monto
                self.operaciones += 1
                self._ops_var.set(f"Ops: {self.operaciones}/{MAX_OPERACIONES}")
                self._show_msg(mensaje, C_GREEN)
            else:
                self._trans_msg.config(text=mensaje, fg=C_RED)
                self.monto_buf = ""
                self._refresh_monto()

    def run(self):
        self.root.mainloop()


# ── PUNTO DE ENTRADA ─────────────────────────────────────────
if __name__ == "__main__":
    app = CajeroApp()
    app.run()
