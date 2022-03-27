# LED MATRIX TELEGRAM-BOT
#### Telegram bot drawing on 8x8 matrix
<hr></hr>

For this you need:
- arduino uno (or arduino compatible board)
- 16 male-female wires
- usb 2.0 A-B(to connect arduino to com port)
- computer with com-port

Pip:
- aiogram
- pySerial
<hr></hr>

#### Connection

Scheme for matrix 8x8:

![led-matrix-8x8](https://user-images.githubusercontent.com/68957520/159114393-23171c57-7537-4486-b20e-a575a4d91741.png)
<br><br><br>
Scheme for connection to arduino board(for example: digital port 2 - R1):

- ROW_1 2  
- ROW_2 3  
- ROW_3 4   
- ROW_4 5  
- ROW_5 6  
- ROW_6 7  
- ROW_7 8   
- ROW_8 9   
<br><br>
- COL_1 10  
- COL_2 11   
- COL_3 12   
- COL_4 13  
<br><br>

Analog connection:
- COL_5 A0   
- COL_6 A1   
- COL_7 A2  
- COL_8 A3 

<hr></hr>

#### Code

1. Open file "config.py" at "LedMatrixTBot\python" and enter bot token(how to get bot-token: https://www.siteguarding.com/en/how-to-get-telegram-bot-api-token), COM-port(the port to which the board is connected. For example: "COM3")
2. Install arduino IDE (https://docs.arduino.cc/software/ide-v1/tutorials/Windows) and upload the sketch to the board from LedMatrixTBot\arduino\ard

<hr></hr>

#### Are you ready?

If you have done everything above, connect the arduino to the correct COM port and run main.py

<hr></hr>

### EXAMPLES

My friend on discord

https://user-images.githubusercontent.com/68957520/159117414-c6b8f66c-0667-4208-aa3c-2c463b445c4a.mp4

<br>

Me

https://user-images.githubusercontent.com/68957520/159117422-f6540de9-b634-4735-885c-25425dcf6fbb.mp4
