# Distance Converter

## Project Overview
This is a tool to convert Miles to Kilometers from a minimalist graphic user interface. 

## Objectives
- A text field for user input.
- A button with the calculate function for user interaction.
- The tool is required to stay open for the user to check multiple conversions.


## Results
![image](https://github.com/frantzalexander/distance_converter/assets/128331579/3dfc945a-d83f-4af4-8e05-4cd291f541a8)






## Process
```mermaid
flowchart TD
start(((START)))
window[Create GUI Window]
field[Text field for User Input]
function[Conversion function utilizing User Input]
conversion[Conversion Output Label]
button[Calculate Button Activates Conversion Function]
finish(((END)))
start --> window
window --> field
field --> function
function --> conversion
conversion --> button
button --> finish
