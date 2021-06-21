function delete_izolation() {
    const MainWindow = new BrowserWindow({
        WebPreferences: {
            contextIzolation: true
        }
    })
    console.log(MainWindow)
};
delete_izolation();