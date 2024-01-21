import tkinter as tk
from tkinter import ttk, font, messagebox
import ipaddress

class VLSMCalculator:
    def __init__(self):
        self.root = tk.Tk()
        self.config_window()
        self.paneles()
        self.controles_barra_superior()  
        self.controles_menu_lateral()
        self.controles_cuerpo()
        self.menu_lateral_visible = True  # Visibilidad del menú lateral

    def paneles(self):
        # Barra superior
        self.barra_superior = tk.Frame(self.root, bg='#1f2329', height=50)
        self.barra_superior.pack(side="top", fill="both")

        # Menú lateral con scrollbar
        self.menu_lateral = tk.Frame(self.root, bg='#2a3138', width=280)
        self.menu_lateral.pack(side=tk.LEFT, fill="both", expand=False)

        self.canvas_menu = tk.Canvas(self.menu_lateral, bg='#2a3138')
        self.scrollbar_menu = tk.Scrollbar(self.menu_lateral, orient="vertical", command=self.canvas_menu.yview)

        self.scrollable_frame_menu = tk.Frame(self.canvas_menu, bg='#2a3138')
        self.scrollable_frame_menu.bind("<Configure>", lambda e: self.canvas_menu.configure(scrollregion=self.canvas_menu.bbox("all")))
        
        self.canvas_menu.create_window((0, 0), window=self.scrollable_frame_menu, anchor="nw")
        self.canvas_menu.configure(yscrollcommand=self.scrollbar_menu.set)
        
        self.canvas_menu.pack(side="left", fill="both", expand=True)
        self.scrollbar_menu.pack(side="right", fill="y")

        # Cuerpo principal
        self.cuerpo_principal = tk.Frame(self.root, bg='#f1faff')
        self.cuerpo_principal.pack(side="right", fill="both", expand=True)


    def controles_barra_superior(self):
        # Configuración de la barra superior
        font_awesome = font.Font(family='FontAwesome', size=12)

        # Etiqueta de título
        self.labelTitulo = tk.Label(self.barra_superior, text="Calculadora VLSM")
        self.labelTitulo.config(fg="#fff", font=("Roboto", 15), bg="#1f2329", pady=10, width=16)
        self.labelTitulo.pack(side=tk.LEFT)
        
        # Botón del menú lateral
        self.buttonMenuLateral = tk.Button(self.barra_superior, text="\uf0c9", font=font_awesome,
                                           command=self.toggle_panel, bd=0, bg="#1f2329", fg="white")
        self.buttonMenuLateral.pack(side=tk.LEFT)
        
        # Etiqueta de información
        self.labelInfo = tk.Label(
            self.barra_superior, text="by @Jhosepe")
        self.labelInfo.config(fg="#fff", font=(
            "Roboto", 10), bg="#1f2329", padx=30, width=5)
        self.labelInfo.pack(side=tk.RIGHT)

    def controles_menu_lateral(self):
        
        self.labelDireccionIP = tk.Label(self.scrollable_frame_menu, text=" ")
        self.labelDireccionIP.config(fg="#f1faff", font=("Terminal", 12), bg="#2a3138", pady=15)
        self.labelDireccionIP.pack(side=tk.TOP, anchor=tk.W, padx=180)
        
        # Widget de entrada para la dirección IP y CIDR
        self.labelDireccionIP = tk.Label(self.scrollable_frame_menu, text="Dirección IP y CIDR:")
        self.labelDireccionIP.config(fg="#f1faff", font=("Terminal", 12), bg="#2a3138", pady=2)
        self.labelDireccionIP.pack(side=tk.TOP, anchor=tk.W, padx=11)
        
        self.entryDireccionIP = tk.Entry(self.scrollable_frame_menu, bg='#f1faff', fg='#1f2329', insertbackground='#1f2329')
        self.entryDireccionIP.config(font=("Terminal", 12), width=20, relief=tk.FLAT, bd=2)
        self.entryDireccionIP.pack(padx=15, pady=(0, 10), anchor=tk.W)
        self.entryDireccionIP.insert(0, "192.168.0.1/24")
        
        # Lista para almacenar los contenedores de Entry
        self.labelSubredes = tk.Label(self.scrollable_frame_menu, text="Cuantas Subredes Necesitas?")
        self.labelSubredes.config(fg="#f1faff", font=("Terminal", 12), bg="#2a3138", pady=2)
        self.labelSubredes.pack(side=tk.TOP, anchor=tk.W, padx=11)

        # Widget Spinbox para seleccionar la cantidad de subredes
        self.spinboxSubredes = tk.Spinbox(self.scrollable_frame_menu, from_=1, to=100, bg='#f1faff', fg='#1f2329', insertbackground='#1f2329', command=self.actualizar_entries)
        self.spinboxSubredes.config(font=("Terminal", 12), width=4, relief=tk.FLAT, bd=2)
        self.spinboxSubredes.pack(padx=15, pady=(0, 10), anchor=tk.W)

        # Lista para almacenar los contenedores de Entry
        self.labelSubredes = tk.Label(self.scrollable_frame_menu, text="Nombre Host  Número Host")
        self.labelSubredes.config(fg="#f1faff", font=("Terminal", 12), bg="#2a3138", pady=2)
        self.labelSubredes.pack(side=tk.TOP, anchor=tk.W, padx=10)

        # Lista para almacenar los contenedores de Entry
        self.contenedores_entry = []
        self.entries_subredes = []  # Mover la inicialización de la lista a este lugar

        # Crear los primeros contenedores de Entry
        self.actualizar_entries()

        # Estilo del botón
        self.root.style = ttk.Style()
        self.root.style.configure("TButton", padding=10, font=("Roboto", 12), background="#1f2329", foreground="#1f2329")
        self.root.style.map("TButton", background=[("active", "#1f2329")])

        # Crear el botón para calcular al final
        self.botonCalcular = ttk.Button(self.scrollable_frame_menu, text="Calcular", style="TButton", command=self.realizar_calculo)
        self.botonCalcular.pack(side=tk.BOTTOM, pady=10, anchor=tk.W, padx=15)

    def actualizar_entries(self):
        # Obtener la cantidad actual de contenedores de Entry
        cantidad_actual = len(self.contenedores_entry)
        
        # Obtener la nueva cantidad de subredes
        cantidad_subredes = int(self.spinboxSubredes.get())

        # Determinar si necesitas agregar o eliminar contenedores
        if cantidad_actual < cantidad_subredes:
            # Necesitas agregar contenedores
            for i in range(cantidad_actual, cantidad_subredes):
                contenedor = tk.Frame(self.scrollable_frame_menu, bg='#2a3138')
                contenedor.pack(side=tk.TOP, anchor=tk.W, padx=10, pady=5)

                entry1 = tk.Entry(contenedor, bg='#f1faff', fg='#1f2329', insertbackground='#1f2329')
                entry1.config(font=("Terminal", 12), width=11, relief=tk.FLAT, bd=2)
                entry1.pack(side=tk.LEFT, padx=5)

                entry2 = tk.Entry(contenedor, bg='#f1faff', fg='#1f2329', insertbackground='#1f2329')
                entry2.config(font=("Terminal", 12), width=11, relief=tk.FLAT, bd=2)
                entry2.pack(side=tk.LEFT, padx=11)

                # Agregar las Entry a la lista
                self.entries_subredes.append((entry1, entry2))
                self.contenedores_entry.append(contenedor)

        elif cantidad_actual > cantidad_subredes:
            # Necesitas eliminar contenedores
            for i in range(cantidad_actual - 1, cantidad_subredes - 1, -1):
                contenedor = self.contenedores_entry.pop()
                contenedor.destroy()

                # Eliminar las Entry de la lista
                self.entries_subredes.pop()


    def realizar_calculo(self):
        try:
            direccion_original = self.entryDireccionIP.get()
            
            red_original = ipaddress.IPv4Network(direccion_original, strict=False)

            # Obtener la cantidad de subredes del Spinbox
            num_subredes = int(self.spinboxSubredes.get())

            subredes = []
            for i, (entry1, entry2) in enumerate(self.entries_subredes[:num_subredes], 1):
                nombre_subred = entry1.get()
                num_hosts = int(entry2.get())
                subredes.append({'nombre': nombre_subred, 'hosts': num_hosts})

            # Llamar a la función para calcular VLSM
            resultados = self.calcular_vlsm(direccion_original, subredes)

            # Ordenar los resultados de mayor a menor cantidad de hosts utilizables
            resultados_ordenados = sorted(resultados, key=lambda x: int(x['cantidad_hosts_utilizables']), reverse=True)

            # Actualizar la tabla con los resultados ordenados
            self.actualizar_tabla(resultados_ordenados)
        except ValueError:
            messagebox.showerror("Error", "Ingrese datos válidos para la dirección IP, cantidad de subredes y número de hosts.")

    def calcular_vlsm(self, direccion_original, subredes):
        resultados = []

        # Convertir la dirección original a un objeto ipaddress
        red_original = ipaddress.IPv4Network(direccion_original, strict=False)

        # Ordenar las subredes por la cantidad de hosts utilizables de mayor a menor
        subredes_ordenadas = sorted(subredes, key=lambda x: x['hosts'], reverse=True)

        # Inicializar la dirección de red actual
        direccion_actual = red_original.network_address

        # Iterar sobre las subredes ordenadas
        for subred in subredes_ordenadas:
            nombre_subred = subred['nombre']
            cantidad_hosts = subred['hosts']

            # Obtener la máscara de CIDR y la cantidad de hosts utilizables
            nueva_mascara_cidr, hosts_utilizables = self.calcular_mascara_hosts_utilizables(cantidad_hosts)

            # Crear la nueva subred
            nueva_subred = ipaddress.IPv4Network((direccion_actual, nueva_mascara_cidr), strict=False)

            # Obtener la máscara de subred en formato decimal
            nueva_mascara_decimal = ".".join(map(str, nueva_subred.netmask.packed))

            # Obtener las direcciones IP utilizables en la subred
            direcciones_utilizables = list(nueva_subred.hosts())

            # Calcular la dirección de broadcast
            direccion_broadcast = nueva_subred.broadcast_address

            # Agregar resultados a la lista
            resultados.append({
                'nombre_subred': nombre_subred,
                'direccion_red': str(direccion_actual),
                'mascara_cidr': f"/{nueva_mascara_cidr}",
                'mascara_decimal': nueva_mascara_decimal,
                'cantidad_hosts_solicitados': str(cantidad_hosts),
                'cantidad_hosts_utilizables': str(hosts_utilizables),
                'rango_ips_utilizables': f"{direcciones_utilizables[0]} - {direcciones_utilizables[-1]}",
                'direccion_broadcast': str(direccion_broadcast),
            })

            # Actualizar la dirección de red actual para la próxima subred
            direccion_actual += nueva_subred.num_addresses

        return resultados


    def calcular_mascara_hosts_utilizables(self, cantidad_hosts):
        #print(f"{cantidad_hosts}")
        if cantidad_hosts == 2:
            # Caso especial para 1 o 2 hosts
            nueva_mascara_cidr = 32 - cantidad_hosts.bit_length()
            hosts_utilizables = 2 ** (32 - nueva_mascara_cidr) - 2
        elif cantidad_hosts == 1:
            # Caso especial para 1 o 2 hosts
            nueva_mascara_cidr = 32 - cantidad_hosts.bit_length()
            hosts_utilizables = 2 ** (32 - nueva_mascara_cidr)
        else:
            # Cálculo estándar con ajuste para excluir dirección de red y broadcast
            nueva_mascara_cidr = 32 - (cantidad_hosts + 2).bit_length()
            hosts_utilizables = 2 ** (32 - nueva_mascara_cidr) - 2
            #print(f"{nueva_mascara_cidr, hosts_utilizables}")
        return nueva_mascara_cidr, hosts_utilizables

    def controles_cuerpo(self):
        # Crea el Treeview para la tabla
        self.tabla = ttk.Treeview(self.cuerpo_principal, columns=("Subred", "Dirección de Red", "CIDR", "Máscara Decimal", "Hosts Solicitados", "Hosts Utilizables", "Rango IPs Utilizables", "Broadcast"))
        # Configura el estilo para agregar líneas de cuadrícula y alternancia de colores
        style = ttk.Style()
        style.configure("Treeview", rowheight=20, font=('Arial', 8), rowmargin=1)
        # Oculta la columna de índices
        self.tabla["show"] = "headings"
        
        # Configura el encabezado de la tabla
        for col in ("Subred", "Dirección de Red", "CIDR", "Máscara Decimal", "Hosts Solicitados", "Hosts Utilizables", "Rango IPs Utilizables", "Broadcast"):
            self.tabla.heading(col, text=col)
            self.tabla.column(col, width=150, anchor=tk.CENTER)

        # Configura el scroll vertical
        scroll_y = ttk.Scrollbar(self.cuerpo_principal, orient="vertical", command=self.tabla.yview)
        self.tabla.configure(yscrollcommand=scroll_y.set)

        # Configura el scroll horizontal
        scroll_x = ttk.Scrollbar(self.cuerpo_principal, orient="horizontal", command=self.tabla.xview)
        self.tabla.configure(xscrollcommand=scroll_x.set)

        # Ubica la tabla, el scroll vertical y el scroll horizontal en el cuerpo principal
        self.tabla.grid(row=0, column=0, sticky="nsew")
        scroll_y.grid(row=0, column=1, sticky="ns")
        scroll_x.grid(row=1, column=0, sticky="ew")

        # Configura el cuerpo principal
        self.cuerpo_principal.grid_rowconfigure(0, weight=1)
        self.cuerpo_principal.grid_rowconfigure(1, weight=0)  # Fila del scroll horizontal
        self.cuerpo_principal.grid_columnconfigure(0, weight=1)

    def actualizar_tabla(self, resultados):
        # Elimina todas las filas actuales
        for i in self.tabla.get_children():
            self.tabla.delete(i)

        # Inserta los nuevos datos en la tabla
        direccion_actual = None  # Variable para almacenar la dirección de red actual

        for resultado in resultados:
            nombre_subred = resultado['nombre_subred']
            direccion_red = resultado['direccion_red']
            mascara_cidr = resultado['mascara_cidr']
            nueva_mascara_decimal = resultado['mascara_decimal']
            cantidad_hosts_solicitados = resultado['cantidad_hosts_solicitados']
            cantidad_hosts_utilizables = resultado['cantidad_hosts_utilizables']
            rango_ips_utilizables = resultado['rango_ips_utilizables']
            direccion_broadcast = resultado['direccion_broadcast']

            # Crear nueva presentación de la dirección de red
            if direccion_actual is None:
                direccion_actual = direccion_red
            presentacion_direccion_red = f"{direccion_actual} - {rango_ips_utilizables}"

            # Agregar fila a la tabla
            self.tabla.insert("", "end", values=(
                nombre_subred,
                direccion_red,
                mascara_cidr,
                nueva_mascara_decimal,
                cantidad_hosts_solicitados,
                cantidad_hosts_utilizables,
                rango_ips_utilizables,
                direccion_broadcast
            ))

    def toggle_panel(self):
        # Alternar visibilidad del menú lateral
        if self.menu_lateral_visible:
            # Ocultar el menú lateral y expandir el cuerpo principal
            self.menu_lateral.pack_forget()
            self.menu_lateral_visible = False
            self.cuerpo_principal.pack(side="right", fill="both", expand=True)
        else:
            # Mostrar el menú lateral y reducir el tamaño del cuerpo principal
            self.menu_lateral.pack(side=tk.LEFT, fill='y')
            self.menu_lateral_visible = True
            self.cuerpo_principal.pack_forget()
            self.root.update_idletasks()  # Actualizar la ventana
            self.menu_lateral.config(width=280)  # Establecer el tamaño fijo del menú lateral
            self.cuerpo_principal.pack(side="right", fill="both", expand=True)
            # Actualizar manualmente el scrollregion
            self.canvas_menu.update_idletasks()
            self.canvas_menu.configure(scrollregion=self.canvas_menu.bbox("all"))
    
    def config_window(self):
        # Configuraciones generales de la ventana principal
        self.root.title("Calculadora VLSM")
        self.root.geometry("1280x400")

    def run(self):
        # Iniciar el bucle principal de la aplicación
        self.root.mainloop()

if __name__ == "__main__":
    calculator_app = VLSMCalculator()
    calculator_app.run()