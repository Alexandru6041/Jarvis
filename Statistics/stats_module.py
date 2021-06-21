class Stats:
    def statistics():
        import sqlite3
        window = tk.Tk()
        title = "Jarvis-Statistics"
        window.geometry("1000x800")
        window.title(title)
        import datetime as dt
        db = SqliteDatabase("info.db")
        class Meta:
            database = db
        current_directory = os.getcwd()
        con = sqlite3.connect(str(current_directory) + "\info.sql")
        window.mainloop()

    def get_stats():
        ok = True
        current_directory = os.getcwd()
        con = sqlite3.connect(str(current_directory) + "\info.sql")
        print("ok")
