#!/bin/bash

echo "1. Addition (+)"
echo "2. Subtraction (-)"
echo "3. Multiplication (*)"
echo "4. Division (/)"
echo "5. Exit"
read -p "Enter Operator (1-5): " choice

if [[ $choice -eq 1 || $choice -eq 2 || $choice -eq 3 || $choice -eq 4 ]]; then
    read -p "Enter the first number: " num1
    read -p "Enter the second number: " num2

    if [[ $choice -eq 1 ]]; then
        echo "$num1 + $num2 = $(bc <<< "$num1 + $num2")"
    elif [[ $choice -eq 2 ]]; then
        echo "$num1 - $num2 = $(bc <<< "$num1 - $num2")"
    elif [[ $choice -eq 3 ]]; then
        echo "$num1 * $num2 = $(bc <<< "$num1 * $num2")"
    elif [[ $choice -eq 4 ]]; then
        if [[ $num2 -eq 0 ]]; then
            echo "Error: Division by zero."
        else
            echo "$num1 / $num2 = $(bc <<< "scale=2; $num1 / $num2")"
        fi
    fi
else [[ $choice -eq 5 ]]; then
    echo "Exiting calculator."
fijn