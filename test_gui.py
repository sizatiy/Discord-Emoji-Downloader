import sys
import traceback

def main():
    try:
        print("Starting application...")
        import tkinter as tk
        from tkinter import messagebox
        print("Tkinter imported successfully")
        
        root = tk.Tk()
        root.title("Test Window")
        root.geometry("300x200")
        
        label = tk.Label(root, text="If you see this, it works!")
        label.pack(pady=20)
        
        button = tk.Button(root, text="Click me", command=lambda: messagebox.showinfo("Success", "The app is working!"))
        button.pack()
        
        print("Window created, starting mainloop...")
        root.mainloop()
        print("Application closed")
        
    except Exception as e:
        print(f"ERROR: {e}")
        traceback.print_exc()
        
        # Try to show error in GUI
        try:
            import tkinter as tk
            from tkinter import messagebox
            root = tk.Tk()
            root.withdraw()
            messagebox.showerror("Error", f"{str(e)}\n\nTraceback:\n{traceback.format_exc()}")
        except:
            pass

if __name__ == "__main__":
    main()
