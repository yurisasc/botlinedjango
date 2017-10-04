## TEST TUGAS
## /new

class Reminder():

    def __init__(self):
        self.dictio = {}

    def new_tugas(event, line_bot_api, matkul, tanggal, pesan):
        if matkul in self.dictio: self.dictio[matkul][pesan] = tanggal
        else: self.dictio[matkul] = {pesan:tanggal}
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text="Added task " + pesan + " in " + matkul)
        )

    ## /task date
    def get_tugasInTanggal(event, line_bot_api, tanggal):
        result = "==================\n"
        for tugas in list(self.dictio.values()):
            if tanggal in list(tugas.keys()):
                result += (list(self.dictio.keys())[list(self.dictio.values()).index(tugas)] + " " +tugas.get(tanggal) + "\n")
                print("get_tugasInTanggal")
        result += "=================="
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text=result)
        )

    ## /task course
    def get_tugasInMatkul(event, line_bot_api, matkul):
        result = "==================\n"
        for tugas in self.dictio.get(matkul):
            result += (tugas + " " + self.dictio.get(matkul).get(tugas) + "\n")
            print("get_tugasInMatkul")
        result += "=================="
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text=result)
        )

    ## /course
    def get_courses(event, line_bot_api):
        result = "==================\n"
        for matkul in self.dictio:
            result += (matkul + "\n")
            print("get_courses")
        result += "=================="
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text=result)
        )

    ## /remove
    def remove_tugas(event, line_bot_api, matkul, pesan):
        if matkul in dictio:
            try:
                self.dictio[matkul].pop(pesan)
                line_bot_api.reply_message(
                    event.reply_token,
                    TextSendMessage(text="Removed task " + pesan + " in " + matkul)
                )
            except KeyError:
                line_bot_api.reply_message(
                    event.reply_token,
                    TextSendMessage(text="No such task in the course")
                )
        else:
            line_bot_api.reply_message(
                event.reply_token,
                TextSendMessage(text="Course not found")
            )

    def dictio(event, line_bot_api):
        print("try printing dictio")
        line_bot_api.reply_message(
                event.reply_token,
                TextSendMessage(text=self.dictio)
            )
