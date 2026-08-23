import os
import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk
from gradio_client import Client, handle_file


# =========================================================
# SETTINGS
# =========================================================

SPACE_ID = "yisol/IDM-VTON"

# Do NOT put your Hugging Face token directly in the code.
# Set it in Windows using:
# set HF_TOKEN=your_new_token
HF_TOKEN = ""


# =========================================================
# VARIABLES
# =========================================================

model_image = None
dress_image = None


# =========================================================
# CONNECT TO HUGGING FACE
# =========================================================

def connect_huggingface():

    try:

        if HF_TOKEN:

            client = Client(
                SPACE_ID,
                token=HF_TOKEN
            )

        else:

            client = Client(
                SPACE_ID
            )

        print("Connected to Hugging Face.")

        return client

    except Exception as e:

        messagebox.showerror(
            "Connection Error",
            str(e)
        )

        return None


# =========================================================
# SELECT MODEL
# =========================================================

def select_model():

    global model_image

    filename = filedialog.askopenfilename(

        title="Select Model Photo",

        filetypes=[
            (
                "Image Files",
                "*.jpg *.jpeg *.png *.webp"
            )
        ]
    )

    if not filename:
        return

    model_image = filename

    model_label.config(
        text=os.path.basename(filename)
    )

    show_preview(
        filename,
        model_preview
    )


# =========================================================
# SELECT DRESS
# =========================================================

def select_dress():

    global dress_image

    filename = filedialog.askopenfilename(

        title="Select Dress Photo",

        filetypes=[
            (
                "Image Files",
                "*.jpg *.jpeg *.png *.webp"
            )
        ]
    )

    if not filename:
        return

    dress_image = filename

    dress_label.config(
        text=os.path.basename(filename)
    )

    show_preview(
        filename,
        dress_preview
    )


# =========================================================
# SHOW PREVIEW
# =========================================================

def show_preview(filename, label):

    try:

        image = Image.open(filename)

        image.thumbnail(
            (180, 220)
        )

        photo = ImageTk.PhotoImage(
            image
        )

        label.config(
            image=photo,
            text=""
        )

        label.image = photo

    except Exception as e:

        print(e)


# =========================================================
# GENERATE TRY-ON
# =========================================================

def generate_tryon():

    if model_image is None:

        messagebox.showwarning(
            "Missing Model",
            "Please select the model photo."
        )

        return


    if dress_image is None:

        messagebox.showwarning(
            "Missing Dress",
            "Please select the dress photo."
        )

        return


    generate_button.config(
        state="disabled"
    )

    status_label.config(
        text="Connecting to IDM-VTON..."
    )

    root.update()


    try:

        # =================================================
        # CONNECT
        # =================================================

        client = connect_huggingface()

        if client is None:

            return


        status_label.config(
            text="Uploading images..."
        )

        root.update()


        # =================================================
        # HUMAN IMAGE
        # =================================================

        human_input = {

            "background": handle_file(
                model_image
            ),

            "layers": [],

            "composite": None
        }


        # =================================================
        # GARMENT IMAGE
        # =================================================

        garment_input = handle_file(
            dress_image
        )


        # =================================================
        # GENERATE
        # =================================================

        status_label.config(
            text="Generating... Please wait."
        )

        root.update()


        print(
            "\nSending request to IDM-VTON..."
        )


        # IMPORTANT:
        # IDM-VTON expects "dict", NOT "imgs"

        result = client.predict(

            dict=human_input,

            garm_img=garment_input,

            garment_des="a dress",

            is_checked=True,

            is_checked_crop=False,

            denoise_steps=30,

            seed=42,

            api_name="/tryon"
        )


        print(
            "\nIDM-VTON RESULT:"
        )

        print(result)


        # =================================================
        # GET RESULT IMAGE
        # =================================================

        result_path = None


        if isinstance(result, tuple):

            if len(result) > 0:

                result_path = result[0]


        elif isinstance(result, list):

            if len(result) > 0:

                result_path = result[0]


        elif isinstance(result, str):

            result_path = result


        # =================================================
        # CHECK RESULT
        # =================================================

        if result_path is None:

            raise Exception(
                "No result image returned.\n\n"
                + str(result)
            )


        print(
            "\nGenerated image:"
        )

        print(result_path)


        # =================================================
        # DISPLAY RESULT
        # =================================================

        result_img = Image.open(
            result_path
        )

        result_img.thumbnail(
            (300, 400)
        )


        result_photo = ImageTk.PhotoImage(
            result_img
        )


        result_preview.config(
            image=result_photo,
            text=""
        )


        result_preview.image = result_photo


        # =================================================
        # SAVE RESULT
        # =================================================

        full_result = Image.open(
            result_path
        )


        full_result.save(
            "tryon_result.png"
        )


        # =================================================
        # SUCCESS
        # =================================================

        status_label.config(
            text="Virtual try-on completed!"
        )


        messagebox.showinfo(

            "Success",

            "Virtual try-on completed!\n\n"

            "Saved as:\n"

            "tryon_result.png"
        )


    except Exception as e:

        print(
            "\nERROR:"
        )

        print(e)


        status_label.config(
            text="Generation failed."
        )


        messagebox.showerror(
            "Generation Error",
            str(e)
        )


    finally:

        generate_button.config(
            state="normal"
        )


# =========================================================
# MAIN WINDOW
# =========================================================

root = tk.Tk()

root.title(
    "AI Virtual Try-On"
)

root.geometry(
    "900x700"
)

root.resizable(
    False,
    False
)


# =========================================================
# TITLE
# =========================================================

title = tk.Label(

    root,

    text="AI Virtual Try-On",

    font=(
        "Arial",
        26,
        "bold"
    )
)

title.pack(
    pady=20
)


# =========================================================
# INPUT FRAME
# =========================================================

image_frame = tk.Frame(
    root
)

image_frame.pack(
    pady=10
)


# =========================================================
# MODEL FRAME
# =========================================================

model_frame = tk.Frame(
    image_frame
)

model_frame.grid(
    row=0,
    column=0,
    padx=30
)


tk.Label(

    model_frame,

    text="MODEL",

    font=(
        "Arial",
        16,
        "bold"
    )

).pack(
    pady=10
)


model_preview = tk.Label(

    model_frame,

    text="No Image",

    width=25,

    height=12,

    relief="solid"
)

model_preview.pack()


tk.Button(

    model_frame,

    text="Select Model Photo",

    command=select_model,

    font=(
        "Arial",
        12
    )

).pack(
    pady=10
)


model_label = tk.Label(

    model_frame,

    text="No model selected"
)

model_label.pack()


# =========================================================
# DRESS FRAME
# =========================================================

dress_frame = tk.Frame(
    image_frame
)

dress_frame.grid(
    row=0,
    column=1,
    padx=30
)


tk.Label(

    dress_frame,

    text="DRESS",

    font=(
        "Arial",
        16,
        "bold"
    )

).pack(
    pady=10
)


dress_preview = tk.Label(

    dress_frame,

    text="No Image",

    width=25,

    height=12,

    relief="solid"
)

dress_preview.pack()


tk.Button(

    dress_frame,

    text="Select Dress Photo",

    command=select_dress,

    font=(
        "Arial",
        12
    )

).pack(
    pady=10
)


dress_label = tk.Label(

    dress_frame,

    text="No dress selected"
)

dress_label.pack()


# =========================================================
# GENERATE BUTTON
# =========================================================

generate_button = tk.Button(

    root,

    text="GENERATE TRY-ON",

    command=generate_tryon,

    font=(
        "Arial",
        15,
        "bold"
    ),

    padx=30,

    pady=12
)

generate_button.pack(
    pady=25
)


# =========================================================
# STATUS
# =========================================================

status_label = tk.Label(

    root,

    text="Select model and dress.",

    font=(
        "Arial",
        12
    )
)

status_label.pack(
    pady=10
)


# =========================================================
# RESULT TITLE
# =========================================================

tk.Label(

    root,

    text="RESULT",

    font=(
        "Arial",
        16,
        "bold"
    )

).pack(
    pady=5
)


# =========================================================
# RESULT IMAGE
# =========================================================

result_preview = tk.Label(

    root,

    text="Result will appear here",

    width=40,

    height=10,

    relief="solid"
)

result_preview.pack(
    pady=5
)


# =========================================================
# START
# =========================================================

root.mainloop()
