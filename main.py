from tkinter import *
from queries import *
import mysql.connector

root = Tk()
root.title("Music Manager")
root.geometry("700x400")

db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="kunjm@41",
    database="Music"
)


def add_song():
    for widget in root.winfo_children():
        widget.destroy()

    frame_top = Frame(root)
    frame_top.pack(pady=10)

    # name
    name_frame = Frame(root)
    name_label = Label(name_frame, text="Name", font=('Arial', 24))
    name_label.grid(row=0, column=0, padx=20, pady=20)
    name_entry = Entry(name_frame, font=('Arial', 15))
    name_entry.grid(row=0, column=1, padx=20, pady=10)
    name_frame.pack()

    # album
    album_frame = Frame(root)
    name_label = Label(album_frame, text="Album", font=('Arial', 24))
    name_label.grid(row=0, column=0, padx=20, pady=20)

    album_options = fetch_albums(db)
    selected_album_options = StringVar()
    selected_album_options.set(album_options[0])
    select_album = OptionMenu(album_frame, selected_album_options, *album_options)
    select_album.configure(font=('Arial', 15))
    select_album.grid(row=0, column=1, padx=20, pady=20)

    album_frame.pack()

    # genre
    genre_frame = Frame(root)
    name_label = Label(genre_frame, text="Genre", font=('Arial', 24))
    name_label.grid(row=0, column=0, padx=20, pady=20)

    genre_options = fetch_genres(db)
    selected_genre_options = StringVar()
    selected_genre_options.set(genre_options[0])
    select_genre = OptionMenu(genre_frame, selected_genre_options, *genre_options)
    select_genre.configure(font=('Arial', 15))
    select_genre.grid(row=0, column=1, padx=20, pady=20)

    genre_frame.pack()

    # submit
    def submit():
        name = name_entry.get()
        album = selected_album_options.get().split()[0]
        genre = selected_genre_options.get().split()[0][1]
        add_song_query(db, name, album, genre)
        home()
    submit_frame = Frame(root)
    submit_button = Button(submit_frame, text='Submit', font=('Arial', 15), command=submit)
    submit_button.grid(row=0, column=0, padx=20, pady=25)

    cancel_button = Button(submit_frame, text='Cancel', font=('Arial', 15), command=home)
    cancel_button.grid(row=0, column=1, padx=20, pady=25)
    submit_frame.pack()


def add_album():
    for widget in root.winfo_children():
        widget.destroy()

    frame_top = Frame(root)
    frame_top.pack(pady=10)

    # name
    name_frame = Frame(root)
    name_label = Label(name_frame, text="Name", font=('Arial', 24))
    name_label.grid(row=0, column=0, padx=20, pady=20)
    name_entry = Entry(name_frame, font=('Arial', 15))
    name_entry.grid(row=0, column=1, padx=20, pady=10)
    name_frame.pack()

    # singer
    singer_frame = Frame(root)
    name_label = Label(singer_frame, text="Singer", font=('Arial', 24))
    name_label.grid(row=0, column=0, padx=20, pady=20)

    singer_options = fetch_singers(db)  # query singer names
    selected_singer_options = StringVar()
    selected_singer_options.set(singer_options[0])
    select_singer = OptionMenu(singer_frame, selected_singer_options, *singer_options)
    select_singer.configure(font=('Arial', 15))
    select_singer.grid(row=0, column=1, padx=20, pady=20)

    singer_frame.pack()

    # submit
    def submit():
        name = name_entry.get()
        singer = selected_singer_options.get().split()[0]
        add_album_query(db, name, singer)
        home()
    submit_frame = Frame(root)
    submit_button = Button(submit_frame, text='Submit', font=('Arial', 15), command=submit)
    submit_button.grid(row=0, column=0, padx=20, pady=25)

    cancel_button = Button(submit_frame, text='Cancel', font=('Arial', 15), command=home)
    cancel_button.grid(row=0, column=1, padx=20, pady=25)
    submit_frame.pack()


def add_singer():
    for widget in root.winfo_children():
        widget.destroy()

    frame_top = Frame(root)
    frame_top.pack(pady=10)

    # name
    name_frame = Frame(root)
    name_label = Label(name_frame, text="Name", font=('Arial', 24))
    name_label.grid(row=0, column=0, padx=20, pady=20)
    name_entry = Entry(name_frame, font=('Arial', 15))
    name_entry.grid(row=0, column=1, padx=20, pady=10)
    name_frame.pack()

    # gender
    gender_frame = Frame(root)
    gender_label = Label(gender_frame, text="Gender", font=('Arial', 24))
    gender_label.grid(row=0, column=0, padx=20, pady=20)

    gender_var = StringVar()
    male_radio = Radiobutton(gender_frame, text="Male", variable=gender_var, value="Male", font=('Arial', 15))
    male_radio.grid(row=0, column=1, padx=10, pady=5)

    female_radio = Radiobutton(gender_frame, text="Female", variable=gender_var, value="Female", font=('Arial', 15))
    female_radio.grid(row=0, column=2, padx=10, pady=5)
    gender_frame.pack()

    # submit
    def submit():
        name = name_entry.get()
        gender = gender_var.get()
        add_singer_query(db, name, gender)
        home()
    submit_frame = Frame(root)
    submit_button = Button(submit_frame, text='Submit', font=('Arial', 15), command=submit)
    submit_button.grid(row=0, column=0, padx=20, pady=25)

    cancel_button = Button(submit_frame, text='Cancel', font=('Arial', 15), command=home)
    cancel_button.grid(row=0, column=1, padx=20, pady=25)
    submit_frame.pack()


def home():
    for widget in root.winfo_children():
        widget.destroy()

    frame_top = Frame(root)
    frame_top.pack(pady=10)

    search_label = Label(root, text='Search song using', font=('Arial', 24))
    search_label.pack(padx=20, pady=20)

    search_options = ['Song name', 'Album', 'Genre']
    selected_options = StringVar()
    selected_options.set(search_options[0])
    search_using = OptionMenu(root, selected_options, *search_options)
    search_using.configure(font=('Arial', 15))
    search_using.pack(padx=20, pady=10)

    search_frame = Frame(root)

    search_name = Entry(search_frame)
    search_name.configure(width=20, font=('Arial', 15))
    search_name.grid(row=0, column=0, padx=20, pady=10)

    search_button = Button(search_frame, text='Search', font=('Arial', 10), command=song_list)
    search_button.grid(row=0, column=1, padx=20, pady=25)

    search_frame.pack()

    frame_middle = Frame(root)
    frame_middle.pack(pady=20)

    others_frame = Frame(root)
    # add song
    add_song_button = Button(others_frame, text='Add song', font=('Arial', 15), command=add_song)
    add_song_button.grid(row=0, column=0, padx=30, pady=10)

    # add album
    add_album_button = Button(others_frame, text='Add album', font=('Arial', 15), command=add_album)
    add_album_button.grid(row=0, column=1, padx=30, pady=10)

    # add singer
    add_singer_button = Button(others_frame, text='Add singer', font=('Arial', 15), command=add_singer)
    add_singer_button.grid(row=0, column=3, padx=30, pady=10)

    others_frame.configure()
    others_frame.pack()


def song_list():
    for widget in root.winfo_children():
        widget.destroy()

    frame_top = Frame(root)
    frame_top.pack(pady=20)

    songs = {'id1': 'name1', 'id2': 'name2', 'id3': 'name3'}  # query for search song
    for song_id in songs:
        frame = Frame(root)
        # name
        name_label = Label(frame, text=songs[song_id], font=('Arial', 24))
        name_label.grid(row=0, column=0, padx=20, pady=20)

        # view
        view_button = Button(frame, text='View', font=('Arial', 15), command=view_song)
        view_button.grid(row=0, column=1, padx=20, pady=25)

        # edit
        edit_button = Button(frame, text='Edit', font=('Arial', 15), command=edit_song)
        edit_button.grid(row=0, column=2, padx=20, pady=25)

        # delete
        delete_button = Button(frame, text='Delete', font=('Arial', 15))
        delete_button.grid(row=0, column=3, padx=20, pady=25)

        frame.pack()

    cancel_button = Button(root, text='Cancel', font=('Arial', 15), command=home)
    cancel_button.pack(padx=20, pady=25)


def view_song():
    for widget in root.winfo_children():
        widget.destroy()

    frame_top = Frame(root)
    frame_top.pack(pady=10)

    # name
    name_frame = Frame(root)
    name_label = Label(name_frame, text="Name:", font=('Arial', 20))
    name_label.grid(row=0, column=0, padx=20, pady=10)
    name_value = Label(name_frame, text="name_of_song", font=('Arial', 20)) # query song
    name_value.grid(row=0, column=1, padx=20, pady=10)
    name_frame.pack()

    # date
    date_frame = Frame(root)
    date_label = Label(date_frame, text="Date:", font=('Arial', 20))
    date_label.grid(row=0, column=0, padx=20, pady=10)
    date_value = Label(date_frame, text="date_name", font=('Arial', 20))
    date_value.grid(row=0, column=1, padx=20, pady=10)
    date_frame.pack()

    # album
    album_frame = Frame(root)
    album_label = Label(album_frame, text="Album:", font=('Arial', 20))
    album_label.grid(row=0, column=0, padx=20, pady=10)
    album_value = Label(album_frame, text="album_name", font=('Arial', 20))
    album_value.grid(row=0, column=1, padx=20, pady=10)
    album_frame.pack()

    # singer
    singer_frame = Frame(root)
    singer_label = Label(singer_frame, text="Singer:", font=('Arial', 20))
    singer_label.grid(row=0, column=0, padx=20, pady=10)
    singer_value = Label(singer_frame, text="singer_name", font=('Arial', 20))
    singer_value.grid(row=0, column=1, padx=20, pady=10)
    singer_frame.pack()

    # genre
    genre_frame = Frame(root)
    genre_label = Label(genre_frame, text="Genre:", font=('Arial', 20))
    genre_label.grid(row=0, column=0, padx=20, pady=10)
    genre_value = Label(genre_frame, text="genre_name", font=('Arial', 20))
    genre_value.grid(row=0, column=1, padx=20, pady=10)
    genre_frame.pack()

    cancel_button = Button(root, text='Cancel', font=('Arial', 15), command=home)
    cancel_button.pack(padx=20, pady=15)


def edit_song():
    for widget in root.winfo_children():
        widget.destroy()

    frame_top = Frame(root)
    frame_top.pack(pady=10)

    # name
    name_frame = Frame(root)
    name_label = Label(name_frame, text="Name", font=('Arial', 24))
    name_label.grid(row=0, column=0, padx=20, pady=20)
    name_button = Entry(name_frame, font=('Arial', 15))
    name_button.grid(row=0, column=1, padx=20, pady=10)
    name_frame.pack()

    # album
    album_frame = Frame(root)
    name_label = Label(album_frame, text="Album", font=('Arial', 24))
    name_label.grid(row=0, column=0, padx=20, pady=20)

    album_options = ['kohinoor', 'kal ho na ho', 'pk']  # query album names
    selected_album_options = StringVar()
    selected_album_options.set(album_options[0])
    select_album = OptionMenu(album_frame, selected_album_options, *album_options)
    select_album.configure(font=('Arial', 15))
    select_album.grid(row=0, column=1, padx=20, pady=20)

    album_frame.pack()

    # genre
    genre_frame = Frame(root)
    name_label = Label(genre_frame, text="Genre", font=('Arial', 24))
    name_label.grid(row=0, column=0, padx=20, pady=20)

    genre_options = ['hip hop', 'romantic', 'pop']  # query album names
    selected_genre_options = StringVar()
    selected_genre_options.set(genre_options[0])
    select_genre = OptionMenu(genre_frame, selected_genre_options, *genre_options)
    select_genre.configure(font=('Arial', 15))
    select_genre.grid(row=0, column=1, padx=20, pady=20)

    genre_frame.pack()

    # submit
    submit_frame = Frame(root)
    submit_button = Button(submit_frame, text='Submit', font=('Arial', 15))
    submit_button.grid(row=0, column=0, padx=20, pady=25)

    cancel_button = Button(submit_frame, text='Cancel', font=('Arial', 15), command=home)
    cancel_button.grid(row=0, column=1, padx=20, pady=25)
    submit_frame.pack()


home()
root.mainloop()
db.close()
