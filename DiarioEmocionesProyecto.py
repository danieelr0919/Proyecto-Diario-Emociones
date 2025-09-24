import tkinter as tk
from tkinter import ttk, messagebox
from tkcalendar import DateEntry
import mysql.connector

# ----------------------------------------
# CLASE PRINCIPAL: DiarioEmocionesApp
# ----------------------------------------
class DiarioEmocionesApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Diario de Emociones 🧠❤️")
        self.root.geometry("900x700")
        self.root.configure(bg="#faf3e0")

        # Conexión a MySQL
        self.conn = self.crear_conexion_mysql()

        # Configurar estilo
        self.configurar_estilo()

        # Crear interfaz modular
        self.crear_notebook()
        self.crear_pestañas()
        self.crear_footer()

    def crear_conexion_mysql(self):

        try:
            conexion = mysql.connector.connect(
                host='localhost',
                database='diario_emociones',
                user='root',
                password=''  # Cambia si usas contraseña
            )
            if conexion.is_connected():
                print("✅ Conexión a base de datos exitosa")
                return conexion
        except Exception as e:
            print(f"❌ Error de conexión: {e}")

            return None

    def configurar_estilo(self):
        style = ttk.Style()
        style.theme_use('clam')
        style.configure("TNotebook", background="#faf3e0")
        style.configure("TNotebook.Tab",
                        background="#e0d3c1",
                        foreground="#5a4a42",
                        font=("Arial", 11, "bold"),
                        padding=[12, 6])
        style.map("TNotebook.Tab",
                  background=[("selected", "#d4a5a5")],
                  foreground=[("selected", "white")])

    def crear_notebook(self):
        self.notebook = ttk.Notebook(self.root)
        self.notebook.pack(expand=True, fill="both", padx=20, pady=20)

    def crear_pestañas(self):
        # Módulo 1: Usuarios
        self.tab_usuarios = ttk.Frame(self.notebook)
        self.notebook.add(self.tab_usuarios, text=" 👤 Usuarios ")
        self.crear_formulario_usuarios()

        # Módulo 2: Emociones
        self.tab_emociones = ttk.Frame(self.notebook)
        self.notebook.add(self.tab_emociones, text=" 😊 Emociones ")
        self.crear_formulario_emociones()

        # Módulo 3: Entradas
        self.tab_entradas = ttk.Frame(self.notebook)
        self.notebook.add(self.tab_entradas, text=" 📖 Entradas ")
        self.crear_formulario_entradas()

        # Módulo 4: Reportes
        self.tab_reportes = ttk.Frame(self.notebook)
        self.notebook.add(self.tab_reportes, text=" 📈 Reportes ")
        self.crear_formulario_reportes()

    # ----------------------------------------
    # MÓDULO 1: USUARIOS
    # ----------------------------------------
    def crear_formulario_usuarios(self):
        titulo = tk.Label(self.tab_usuarios, text="👤 Gestión de Usuarios", font=("Arial", 16, "bold"), fg="#b86d6d", bg="#faf3e0")
        titulo.pack(pady=(20, 10))

        form_frame = tk.Frame(self.tab_usuarios, bg="#f8f0e3", padx=20, pady=20, relief="groove", bd=1)
        form_frame.pack(pady=10, padx=20, fill="x")

        tk.Label(form_frame, text="ID Usuario:", bg="#f8f0e3", font=("Arial", 12)).grid(row=0, column=0, sticky="w", pady=5)
        self.usuario_id_entry = tk.Entry(form_frame, width=30)
        self.usuario_id_entry.grid(row=0, column=1, sticky="w", pady=5)

        tk.Label(form_frame, text="Username:", bg="#f8f0e3", font=("Arial", 12)).grid(row=1, column=0, sticky="w", pady=5)
        self.username_entry = tk.Entry(form_frame, width=30)
        self.username_entry.grid(row=1, column=1, sticky="w", pady=5)

        tk.Label(form_frame, text="Email:", bg="#f8f0e3", font=("Arial", 12)).grid(row=2, column=0, sticky="w", pady=5)
        self.email_entry = tk.Entry(form_frame, width=30)
        self.email_entry.grid(row=2, column=1, sticky="w", pady=5)

        tk.Label(form_frame, text="Contraseña:", bg="#f8f0e3", font=("Arial", 12)).grid(row=3, column=0, sticky="w", pady=5)
        self.password_entry = tk.Entry(form_frame, width=30, show="*")
        self.password_entry.grid(row=3, column=1, sticky="w", pady=5)

        btn_frame = tk.Frame(self.tab_usuarios, bg="#faf3e0")
        btn_frame.pack(pady=20)

        tk.Button(btn_frame, text="💾 Guardar", bg="#88c9a1", fg="white", width=12,
                  command=self.guardar_usuario).pack(side=tk.LEFT, padx=5)
        tk.Button(btn_frame, text="✏️ Actualizar", bg="#a2b9bc", fg="white", width=12,
                  command=self.actualizar_usuario).pack(side=tk.LEFT, padx=5)
        tk.Button(btn_frame, text="🗑️ Eliminar", bg="#e77f67", fg="white", width=12,
                  command=self.eliminar_usuario).pack(side=tk.LEFT, padx=5)
        tk.Button(btn_frame, text="🧹 Limpiar", bg="#f5c091", fg="#5a4a42", width=12,
                  command=self.limpiar_usuario).pack(side=tk.LEFT, padx=5)

    # FUNCIONES USUARIO
    def guardar_usuario(self):
        username = self.username_entry.get()
        email = self.email_entry.get()
        password = self.password_entry.get()

        if not username or not email or not password:
            messagebox.showwarning("Advertencia", "Todos los campos son obligatorios")
            return

        messagebox.showinfo("Exito", f"Usuario {username} ha sido guardado correctamente")

    def actualizar_usuario(self):
        user_id = self.usuario_id_entry.get()
        if not user_id:
            messagebox.showwarning("Advertencia", "ID de usuario es obligatorio para actualizar")
            return
        messagebox.showinfo("Exito", f"Usuario con ID {user_id} actualizado correctamente")


    def eliminar_usuario(self):
        user_id = self.usuario_id_entry.get()
        if not user_id:
            messagebox.showwarning("Advertencia", "ID de usuario es obligatorio")
            return

        if messagebox.askyesno("Confirmar", "¿Estas seguro de eliminar a este usuario?"):
            messagebox.showinfo("Exito", f"Usuario con ID {user_id} eliminado correctamente")
            self.limpiar_usuario()

    def limpiar_usuario(self):
        self.usuario_id_entry.delete(0, tk.END)
        self.username_entry.delete(0, tk.END)
        self.email_entry.delete(0, tk.END)
        self.password_entry.delete(0, tk.END)

    # ----------------------------------------
    # MÓDULO 2: EMOCIONES
    # ----------------------------------------
    def crear_formulario_emociones(self):
        titulo = tk.Label(self.tab_emociones, text="😊 Catálogo de Emociones", font=("Arial", 16, "bold"), fg="#b86d6d", bg="#faf3e0")
        titulo.pack(pady=(20, 10))

        form_frame = tk.Frame(self.tab_emociones, bg="#f8f0e3", padx=20, pady=20, relief="groove", bd=1)
        form_frame.pack(pady=10, padx=20, fill="x")

        tk.Label(form_frame, text="ID Emoción:", bg="#f8f0e3", font=("Arial", 12)).grid(row=0, column=0, sticky="w", pady=5)
        self.emocion_id_entry = tk.Entry(form_frame, width=30)
        self.emocion_id_entry.grid(row=0, column=1, sticky="w", pady=5)

        tk.Label(form_frame, text="Nombre:", bg="#f8f0e3", font=("Arial", 12)).grid(row=1, column=0, sticky="w", pady=5)
        self.nombre_emocion_entry = tk.Entry(form_frame, width=30)
        self.nombre_emocion_entry.grid(row=1, column=1, sticky="w", pady=5)

        tk.Label(form_frame, text="Emoji:", bg="#f8f0e3", font=("Arial", 12)).grid(row=2, column=0, sticky="w", pady=5)
        self.emoji_entry = tk.Entry(form_frame, width=30)
        self.emoji_entry.grid(row=2, column=1, sticky="w", pady=5)

        btn_frame = tk.Frame(self.tab_emociones, bg="#faf3e0")
        btn_frame.pack(pady=20)

        tk.Button(btn_frame, text="💾 Guardar", bg="#88c9a1", fg="white", width=12,
                  command=self.guardar_emocion).pack(side=tk.LEFT, padx=5)
        tk.Button(btn_frame, text="✏️ Actualizar", bg="#a2b9bc", fg="white", width=12,
                  command=self.actualizar_emocion).pack(side=tk.LEFT, padx=5)
        tk.Button(btn_frame, text="🗑️ Eliminar", bg="#e77f67", fg="white", width=12,
                  command=self.eliminar_emocion).pack(side=tk.LEFT, padx=5)
        tk.Button(btn_frame, text="🧹 Limpiar", bg="#f5c091", fg="#5a4a42", width=12,
                  command=self.limpiar_emocion).pack(side=tk.LEFT, padx=5)

    # FUNCIONES MODULO 2 :
    def guardar_emocion(self):
        nombre = self.nombre_emocion_entry.get()
        emoji = self.emoji_entry.get()

        if not nombre:
            messagebox.showwarning("Advertencia", "El nombre de la emocion es obligatorio")
            return

        messagebox.showinfo("Exito", f"Emocion {nombre} guardada correctamente")

    def actualizar_emocion(self):
        emocion_id = self.emocion_id_entry.get()
        if not emocion_id:
            messagebox.showwarning("Advertencia", "ID de la emocion es obligatorio")
            return
        messagebox.showinfo("Exito", f"Emocion con ID {emocion_id} actualizada correctamente")

    def eliminar_emocion(self):
        emocion_id = self.emocion_id_entry.get()
        if not emocion_id:
            messagebox.showwarning("Advertencia", "ID de la emocion es obligatorio")
            return

        if messagebox.askyesno("Confirmar", "¿Estas seguro de eliminar esta emocion?"):
            messagebox.showinfo("Exito", f"Emocion con ID {emocion_id} eliminada correctamente")
            self.limpiar_emocion()

    def limpiar_emocion(self):
        self.emocion_id_entry.delete(0, tk.END)
        self.nombre_emocion_entry.delete(0, tk.END)
        self.emoji_entry.delete(0, tk.END)

    # ----------------------------------------
    # MÓDULO 3: ENTRADAS
    # ----------------------------------------
    def crear_formulario_entradas(self):
        titulo = tk.Label(self.tab_entradas, text="📖 Entradas del Diario", font=("Arial", 16, "bold"), fg="#b86d6d", bg="#faf3e0")
        titulo.pack(pady=(20, 10))

        form_frame = tk.Frame(self.tab_entradas, bg="#f8f0e3", padx=20, pady=20, relief="groove", bd=1)
        form_frame.pack(pady=10, padx=20, fill="x")

        tk.Label(form_frame, text="ID Entrada:", bg="#f8f0e3", font=("Arial", 12)).grid(row=0, column=0, sticky="w", pady=5)
        self.entrada_id_entry = tk.Entry(form_frame, width=30)
        self.entrada_id_entry.grid(row=0, column=1, sticky="w", pady=5)

        tk.Label(form_frame, text="Usuario ID:", bg="#f8f0e3", font=("Arial", 12)).grid(row=1, column=0, sticky="w", pady=5)
        self.entrada_usuario_id_entry = tk.Entry(form_frame, width=30)
        self.entrada_usuario_id_entry.grid(row=1, column=1, sticky="w", pady=5)

        tk.Label(form_frame, text="Fecha:", bg="#f8f0e3", font=("Arial", 12)).grid(row=2, column=0, sticky="w", pady=5)
        self.fecha_entry = DateEntry(form_frame, width=28, date_pattern="yyyy-mm-dd")
        self.fecha_entry.grid(row=2, column=1, sticky="w", pady=5)

        tk.Label(form_frame, text="Texto:", bg="#f8f0e3", font=("Arial", 12)).grid(row=3, column=0, sticky="nw", pady=5)
        self.texto_entry = tk.Text(form_frame, width=30, height=5)
        self.texto_entry.grid(row=3, column=1, sticky="w", pady=5)

        tk.Label(form_frame, text="Emociones (IDs):", bg="#f8f0e3", font=("Arial", 12)).grid(row=4, column=0, sticky="w", pady=5)
        self.emociones_ids_entry = tk.Entry(form_frame, width=30)
        self.emociones_ids_entry.grid(row=4, column=1, sticky="w", pady=5)

        btn_frame = tk.Frame(self.tab_entradas, bg="#faf3e0")
        btn_frame.pack(pady=20)

        tk.Button(btn_frame, text="💾 Guardar", bg="#88c9a1", fg="white", width=12,
                  command=self.guardar_entrada).pack(side=tk.LEFT, padx=5)
        tk.Button(btn_frame, text="✏️ Actualizar", bg="#a2b9bc", fg="white", width=12,
                  command=self.actualizar_entrada).pack(side=tk.LEFT, padx=5)
        tk.Button(btn_frame, text="🗑️ Eliminar", bg="#e77f67", fg="white", width=12,
                  command=self.eliminar_entrada).pack(side=tk.LEFT, padx=5)
        tk.Button(btn_frame, text="🧹 Limpiar", bg="#f5c091", fg="#5a4a42", width=12,
                  command=self.limpiar_entrada).pack(side=tk.LEFT, padx=5)

    # FUNCIONES MODULO 3:
    def guardar_entrada(self):
        usuario_id = self.entrada_usuario_id_entry.get()
        texto = self.texto_entry.get()
        emociones_ids = self.emociones_ids_entry.get()

        if not usuario_id or not texto:
            messagebox.showwarning("Advertencia", "Usuario ID y Texto son obligatorios")
            return

        messagebox.showinfo("Exito", f"Entrada guardada para Usuario ID: {usuario_id}")

    def actualizar_entrada(self):
        entrada_id = self.entrada_id_entry.get()
        if not entrada_id:
            messagebox.showwarning("Advertencia", "ID de entrada es obligatorio")
            return
        messagebox.showinfo("Exito", f"Entrada actualizada para ID: {entrada_id}")

    def eliminar_entrada(self):
        entrada_id = self.entrada_id_entry.get()
        if not entrada_id:
            messagebox.showwarning("Advertencia", "ID de entrada es obligatorio")
            return

        if messagebox.askyesno("Confirmar","¿Estas seguro de eliminar esta entrada?"):
            messagebox.showinfo("Exito", f"Entrada con ID {entrada_id} eliminada")
            self.limpiar_entrada()


    def limpiar_entrada(self):
        self.entrada_id_entry.delete(0, tk.END)
        self.entrada_usuario_id_entry.delete(0, tk.END)
        self.fecha_entry.delete(0, tk.END)
        self.texto_entry.delete("1.0", tk.END)
        self.emociones_ids_entry.delete(0, tk.END)

    # ----------------------------------------
    # MÓDULO 4: REPORTES
    # ----------------------------------------
    def crear_formulario_reportes(self):
        titulo = tk.Label(self.tab_reportes, text="📈 Resumen Emocional", font=("Arial", 16, "bold"), fg="#b86d6d", bg="#faf3e0")
        titulo.pack(pady=(20, 10))

        form_frame = tk.Frame(self.tab_reportes, bg="#f8f0e3", padx=20, pady=20, relief="groove", bd=1)
        form_frame.pack(pady=10, padx=20, fill="x")

        tk.Label(form_frame, text="Selecciona un usuario (ID):", bg="#f8f0e3", font=("Arial", 12)).grid(row=0, column=0, sticky="w", pady=5)
        self.reporte_usuario_id_entry = tk.Entry(form_frame, width=30)
        self.reporte_usuario_id_entry.grid(row=0, column=1, sticky="w", pady=5)

        tk.Label(form_frame, text="Período:", bg="#f8f0e3", font=("Arial", 12)).grid(row=1, column=0, sticky="w", pady=5)
        self.periodo_var = tk.StringVar(value="semana")
        ttk.Radiobutton(form_frame, text="Semana", variable=self.periodo_var, value="semana").grid(row=1, column=1, sticky="w")
        ttk.Radiobutton(form_frame, text="Mes", variable=self.periodo_var, value="mes").grid(row=1, column=2, sticky="w")

        btn_frame = tk.Frame(self.tab_reportes, bg="#faf3e0")
        btn_frame.pack(pady=20)

        tk.Button(btn_frame, text="📊 Generar Reporte", bg="#88c9a1", fg="white", width=20,
                  command=self.generar_reporte).pack(padx=5)

    def generar_reporte(self):
        usuario_id = self.reporte_usuario_id_entry.get()
        periodo = self.periodo_var.get()

        if not usuario_id:
            messagebox.showwarning("Advertencia", "Por favor, Ingrese un ID de usuario para generar reporte")

    def crear_footer(self):
        footer = tk.Label(self.root, text="Diario de Emociones v1.0 — Tu espacio seguro para sentir 🌿",
                          font=("Arial", 10, "italic"), fg="#7d6e65", bg="#faf3e0")
        footer.pack(side=tk.BOTTOM, pady=15)

# ----------------------------------------
# INICIAR LA APLICACIÓN
# ----------------------------------------
if __name__ == "__main__":
    root = tk.Tk()
    app = DiarioEmocionesApp(root)

    root.mainloop()
