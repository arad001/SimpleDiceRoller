# This program is free software: you can redistribute it and/or modify it under 
# the terms of the GNU General Public License as published by the Free Software 
# Foundation, either version 3 of the License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful, but 
# WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY 
# or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for 
# more details.
#
# You should have received a copy of the GNU General Public License along
#  with this program. If not, see <https://www.gnu.org/licenses/>.


import tkinter as tk
import random 
# importing some basic gui libs

dice_count = 1 
result = ""
res_sum = 0
# declaring some variables to work with

def update_amount():
    global dice_count
    dice_count = spinbox.get()
    # This function determines how many dice is chosen in the spinbox. Don't think there is 
    # anything to change for your personal perferences

def roll_the_dice():
    global dice_count
    global result
    global res_sum
    result = "" # there will be the result of the dice rolls in this string
    res_sum = 0 # and this variable is for the sum of all the results
    for i in range(int(dice_count)):
        # declaring an RNG from 1 to 6
        # you can change it to anything
        temp_num = random.randint(1, 6)
        result += str(temp_num)
        res_sum += temp_num 
        # combining all the rolls in to 1 string 
        # and formatting it to look better which is the "result" variable
    result = (result.replace("", ",")).strip(",")
    # checking if the amount of dice chosen is equal to 1 or not
    if dice_count != 1: 
        # adding the sum at the end after a colon 
        # ex. output with 2 dice: "5,3 : 8"
        result = result + " : %s" % res_sum
    # finally creating a label
    res_label.config(text = result)

# creating a resizable window 
root = tk.Tk()
root.geometry("700x400")
root.resizable(True, True)
root.title("SimpleDiceRoller")

label = tk.Label(root, text = "Simple dice roller", font = ("Arial", 20))
label.pack(pady = 20)

# creating a frame to put the "Amount of dice:" label and the spinbox side by side
frame = tk.Frame(root)
frame.pack()

# the "Amount of dice:" label
label_amount = tk.Label(frame, text = "Amount of dice:", font = ("Arial", 16))
label_amount.grid(row = 0, column = 0, padx = 2, pady = 2)

# the spinbox
spinbox = tk.Spinbox(frame, width = 2, from_ = 1, to_ = 10, font = ("Arial", 16), command = update_amount)
spinbox.grid(row = 0, column = 1, padx = 2, pady = 2)

# the button to roll the dice
btn_roll = tk.Button(root, text = "Roll the dice", font = ("Arial", 18), command = roll_the_dice)
btn_roll.pack(padx = 5, pady = 20)

# the output of the final result
res_label = tk.Label(root, textvariable = result, font = ("Arial", 18))
res_label.pack()

root.mainloop() 