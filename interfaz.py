from cProfile import label
import tkinter as tk
import tkinter.filedialog as fd
import tkinter.messagebox as mb
import main as m

class Aplicacion(tk.Tk):
    
    def __init__(self):
        super().__init__()
        
        self.inicializar_gui()
        
    def inicializar_gui(self):
        self.title('Selector de archivos y carpetas')
        self.geometry('600x550')
        
        btn_seleccionar_archivo = tk.Button(self, text='Seleccionar archivo...')
        btn_seleccionar_archivo['command'] = self.seleccionar_archivo
        
        btn_seleccionar_archivo.pack(padx=60, pady=60)
    
        
    def seleccionar_archivo(self):
        archivo = fd.askopenfilename(
            initialdir='./',
            title='Seleccionar archivo',
            filetypes=(('Archivos de texto', '*.txt'),)
        )
        print(archivo)
        
        if archivo:
            # m.main(archivo)
            
            mb.showinfo('Archivo seleccionado: ', archivo)
            
            btn_validar = tk.Button(self, text='Validar')
            btn_validar['command'] = lambda:m.main(archivo)
            btn_validar.pack(padx=60, pady=10)
            
            btn_seleccionar_carpeta = tk.Button(self, text='Seleccionar carpeta para guardar el reporte...')
            btn_seleccionar_carpeta['command'] = self.seleccionar_carpeta
            
            btn_seleccionar_carpeta.pack(padx=150, pady=60)
                
    
    def seleccionar_carpeta(self):
        
        directorio = fd.askdirectory(
            initialdir='./',
            title='Seleccionar carpeta'
        )
        
        print(directorio)
        
        if directorio:
            mb.showinfo('Carpeta seleccionada: ', directorio)
            
            btn_generar = tk.Button(self, text='Generar reporte')
            btn_generar['command'] = lambda:self.reporte(directorio)
            
            btn_generar.pack(padx=150, pady=10)
    
    def reporte(self, directorio):
        m.reporte_excel(directorio)
        mb.showinfo('Reporte: ', 'Generado correctamente')
        
        
def main():
    app = Aplicacion()
    app.mainloop()
    
if __name__ == '__main__':
    main()