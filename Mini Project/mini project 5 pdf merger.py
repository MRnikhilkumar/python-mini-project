import os
import tkinter as tk
from tkinter import filedialog, messagebox
from pypdf import PdfWriter

file_list = []

def select_files():
    files = filedialog.askopenfilenames(title="Select PDFs to merge",
                                        filetypes=[("PDF files", "*.pdf")])
    if files:
        file_list.clear()
        file_list.extend(files)
        listbox.delete(0, tk.END)
        for f in file_list:
            listbox.insert(tk.END, os.path.basename(f))
        status_label.config(text=f"{len(file_list)} files selected")

def clear_selection():
    file_list.clear()
    listbox.delete(0, tk.END)
    status_label.config(text="No files selected")

def merge_pdfs():
    if not file_list:
        messagebox.showwarning("No files selected", "Please select one or more PDF files to merge.")
        return
    out_path = filedialog.asksaveasfilename(defaultextension=".pdf",
                                            filetypes=[("PDF files", "*.pdf")],
                                            title="Save merged PDF as")
    if not out_path:
        return
    try:
        writer = PdfWriter()
        for pdf in file_list:
            writer.append(pdf)
        writer.write(out_path)
        messagebox.showinfo("Success", f"Merged PDF saved to:\n{out_path}")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to merge PDFs:\n{e}")


def build_ui():
    global root, listbox, status_label
    root = tk.Tk()
    root.title("PDF Merger")
    root.geometry("520x360")

    frame = tk.Frame(root, padx=10, pady=10)
    frame.pack(fill="both", expand=True)

    btn_frame = tk.Frame(frame)
    btn_frame.pack(fill="x", pady=(0, 10))

    select_btn = tk.Button(btn_frame, text="Select PDFs...", command=select_files)
    select_btn.pack(side="left")

    merge_btn = tk.Button(btn_frame, text="Merge PDFs", command=merge_pdfs)
    merge_btn.pack(side="left", padx=6)

    clear_btn = tk.Button(btn_frame, text="Clear", command=clear_selection)
    clear_btn.pack(side="left")

    listbox = tk.Listbox(frame, height=12)
    listbox.pack(fill="both", expand=True)

    status_label = tk.Label(root, text="No files selected", anchor="w")
    status_label.pack(fill="x", padx=10, pady=(6, 10))

    root.mainloop()


if __name__ == "__main__":
    build_ui()

