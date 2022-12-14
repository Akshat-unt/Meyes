# Meyes - [Eyed cursor Controller] π

[![GitHub license](https://img.shields.io/github/license/Naereen/StrapDown.js.svg)]()

![main](meyes.png)

Imagine controlling your computer with your eyes. This is what Meyes does. It is a simple python script that uses the dlib library to detect the eyes and move the cursor accordingly. It also uses the pyautogui library to click and double click. 

## Installation βοΈ


```bash
pip install -r requirements.txt
```

## Usage

```python
python main.py
```

## Flow of Control π₯

- [x] OpenCV to capture the video from the webcam
- [x] Googleβs MediaPipe to detect the face and the eyes
- [x] PyAutoGUI to move the cursor and click

## Constraints β

- Decent camera quality
- Proper lighting [can't function properly in low lighting]

## Contributing π οΈ

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.
Help us overcome the constraints. βπ»

**it took a whole lot effort to make this possible, would you mind giving us a star / sharing this?** π

## Contributors 
[![Twitter Follow](https://img.shields.io/twitter/follow/AkshatK99016584?style=social)](https://twitter.com/AkshatK99016584)
* maybe you? π

## Acknowledgements π
* [OpenCV](https://opencv.org/)
* [Dlib](http://dlib.net/)
* [PyAutoGUI](https://pyautogui.readthedocs.io/en/latest/)
* [Face Recognition](https://en.wikipedia.org/wiki/Facial_recognition_system)
