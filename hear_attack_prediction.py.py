import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import confusion_matrix, accuracy_score
from tkinter import *
from tkinter import PhotoImage

# Load 

data = pd.read_csv(r"C:\Users\212g1\Desktop\Heart Attack.csv")

# Split features and target variable
x = data.iloc[:, 0:-1]
y = data.iloc[:, -1]

# Split data into training and testing sets
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.1)

# Train the RandomForestClassifier
rf = RandomForestClassifier()
rf.fit(x_train, y_train)

# Predict function
def predict_heart_attack():
    user_input = [float(age.get()), float(gender.get()), float(impluse.get()), float(pressure_high.get()),
                  float(pressur_low.get()), float(glucose.get()), float(kcm.get()), float(troponin.get())]

    # Make prediction
    y_pred = rf.predict([user_input])

 # Set color based on prediction result
    if y_pred == "positive":
            color = "red"
    else:
        color = "green"

    # Display prediction
    prediction_label.config(text="Prediction for Heart Attack: " + str(y_pred),fg=color,font =("Arial",14,"bold"))


# Create GUI window
root = Tk()
root.title("Heart Attack Prediction")

# Label for "ALTS" in red color
alts_label = Label(root, text="Anantha Lakshmi", fg="red", font=("Times New Roman", 40, "bold"))
alts_label.grid(row=0, column=50, columnspan=1)

alts_label = Label(root, text="INSTITUTE OF TECHNOLOGY & SCIENCES", fg="black", font=("Times New Roman", 14, "bold"))
alts_label.grid(row=1, column=50, columnspan=1)

# Label for "HEART ATTACK PREDICTION" in blue color
prediction_label = Label(root, text="HEART ATTACK PREDICTION BY \n III AIML STUDENTS", fg="blue", font=("Arial", 15, "bold"))
prediction_label.grid(row=2, column=50, columnspan=2)

# Labels and entry fields for input variables
Label(root, text="Age:").grid(row=3, column=0)
age = Entry(root)
age.grid(row=3, column=1)

Label(root, text="Gender(Male=1,Female=0):").grid(row=4, column=0)
gender = Entry(root)
gender.grid(row=4, column=1)

Label(root, text="Impulse:").grid(row=5, column=0)
impluse = Entry(root)
impluse.grid(row=5, column=1)

Label(root, text="High Pressure:").grid(row=6, column=0)
pressure_high = Entry(root)
pressure_high.grid(row=6, column=1)

Label(root, text="Low Pressure:").grid(row=7, column=0)
pressur_low = Entry(root)
pressur_low.grid(row=7, column=1)

Label(root, text="Glucose:").grid(row=8, column=0)
glucose = Entry(root)
glucose.grid(row=8, column=1)

Label(root, text="KCM:").grid(row=9, column=0)
kcm = Entry(root)
kcm.grid(row=9, column=1)

Label(root, text="Troponin:").grid(row=10, column=0)
troponin = Entry(root)
troponin.grid(row=10, column=1)

# Reset function
def reset_fields():
    age.delete(0, 'end')
    gender.delete(0, 'end')
    impluse.delete(0, 'end')
    pressure_high.delete(0, 'end')
    pressur_low.delete(0, 'end')
    glucose.delete(0, 'end')
    kcm.delete(0, 'end')
    troponin.delete(0, 'end')
    prediction_label.config(text="")

# Button to trigger prediction
predict_button = Button(root, text="Predict", command=predict_heart_attack)
predict_button.grid(row=11, columnspan=2)

# Button to reset fields
reset_button = Button(root, text="Reset", command=reset_fields)
reset_button.grid(row=11, column=0)

# Label to display prediction
prediction_label = Label(root, text="")
prediction_label.grid(row=13, columnspan=2)

root.mainloop()
