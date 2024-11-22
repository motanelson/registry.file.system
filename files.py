import tkinter as tk
from tkinter import filedialog, messagebox, simpledialog
import csv


class QueryApp:
    def __init__(self, root):
        self.root = root
        self.root.title("help Executor")
        self.root.configure(bg="black")
        
        # Menu principal
        self.menu_bar = tk.Menu(self.root)
        self.root.config(menu=self.menu_bar)

        # Caixa de texto para exibir resultados
        self.result_text = tk.Text(root, bg="black", fg="white", wrap=tk.WORD)
        self.result_text.pack(fill=tk.BOTH, expand=True)

        # Botão para carregar o arquivo .file
        self.load_button = tk.Button(
            root,
            text="Load .file File",
            bg="black",
            fg="white",
            command=self.load_query_file
        )
        self.load_button.pack(pady=10)
        self.titles=[]
        self.texts=[]
        
        

    def load_query_file(self):
        query_path = filedialog.askopenfilename(filetypes=[("help Files", "*.fs")])
        if not query_path:
            return

        try:
            with open(query_path, "r") as file:
                reader = file.read()
                queries = reader.split("\n")

            # Limpa os menus existentes
            self.menu_bar.delete(0, tk.END)
            counter=0
            for row in queries:
                rows=row.split("|")

                
                
                
                if len(rows)>1:
                    # Cria um menu e associa a ação ao submenu
                    menu = tk.Menu(self.menu_bar, tearoff=0)
                    self.titles=self.titles+[rows[0]]
                    self.texts=self.texts+[rows[1].replace("\\n","\n").replace("\\r","\r")]
                    self.menu_bar.add_cascade(label=rows[0], menu=menu)
                    menu.add_command(
                        label=rows[0],
                        command=lambda cf=counter, qc=counter : self.execute_query(cf, qc)
                    )
                counter+=1
        except Exception as e:
            messagebox.showerror("Error", f"Failed to load .fs file: {e}")

    def execute_query(self, cf, cff):
        self.result_text.delete(1.0, tk.END)
        self.result_text.insert(tk.END, self.texts[cff])
        


if __name__ == "__main__":
    root = tk.Tk()
    app = QueryApp(root)
    root.mainloop()

