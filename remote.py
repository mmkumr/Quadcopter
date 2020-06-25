import BlynkLib

# Initialize Blynk
blynk = BlynkLib.Blynk('dG2SwZBhNvt8dHp_miQq2UyQO4JxJK-o')

# Register Virtual Pins
@blynk.VIRTUAL_WRITE(3)
def my_write_handler(value):
    print(value[0])

#@blynk.VIRTUAL_READ(2)
#   def my_read_handler():
#       # this widget will show some time in seconds..
#       blynk.virtual_write(2, int(time.time()))

while True:
    blynk.run()
