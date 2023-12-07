# PNG To ICO
A simple PNG to ICO converter.
![App view](https://github.com/VeronGoggans/PNG-to-ICO/blob/main/img/App%20view.png?raw=true)

### Python packeges

```text
pip install pillow
```
```text
pip install customtkinter
```

For just the script copy this.
```python
def png_to_ico(self):
        file_path = filedialog.askopenfilename()
        if file_path.endswith(self.input_format):
            try:
                png_image = Image.open(file_path)
                new_file_path = file_path.replace(self.input_format, self.output_format)
                png_image.save(new_file_path, format='ICO', sizes=[(png_image.width, png_image.height)])
                print('Conversion Successful')
            except Exception as e:
                print(e)
        else:
            print('Please select a PNG file.')
```
