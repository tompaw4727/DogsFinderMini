import torch
import requests
from bs4 import BeautifulSoup

def perform_pred(loaded_model, transformed_image):
    breeds_list = ['afghan-hound', 'African-hunting-dog', 'airedale-terrier', 'american-staffordshire-terrier',
                   'appenzeller-sennenhunde', 'australian-terrier', 'bedlington-terrier', 'bernese-mountain-dog',
                   'cavalier-king-charles-spaniel', 'border-collie', 'border-terrier', 'boston-terrier',
                   'bouvier-des-flandres', 'brussels-griffon', 'brittany', 'cardigan-welsh-corgi',
                   'chesapeake-bay-retriever', 'chihuahua', 'dandie-dinmont-terrier', 'doberman-pinscher',
                   'English_foxhound', 'english-setter', 'english-springer-spaniel', 'entlebucher-mountain-dog',
                   'american-eskimo-dog', 'french-bulldog', 'german-shepherd-dog', 'german-shorthaired-pointer',
                   'gordon-setter', 'great-dane', 'great-pyrenees', 'greater-swiss-mountain-dog', 'ibizan-hound',
                   'irish-setter', 'irish-terrier', 'irish-water-spaniel', 'irish-wolfhound', 'italian-greyhound',
                   'japanese-chin', 'kerry-blue-terrier', 'labrador-retriever', 'lakeland-terrier', 'leonberger',
                   'lhasa-apso', 'maltese', 'xoloitzuintli', 'newfoundland', 'norfolk-terrier', 'norwegian-elkhound',
                   'norwich-terrier', 'old-english-sheepdog', 'pekingese', 'pembroke-welsh-corgi', 'pomeranian',
                   'rhodesian-ridgeback', 'rottweiler', 'saint-bernard', 'saluki', 'samoyed', 'scottish-terrier',
                   'scottish-deerhound', 'sealyham-terrier', 'shetland-sheepdog', 'shih-tzu', 'siberian-husky',
                   'staffordshire-bull-terrier', 'sussex-spaniel', 'tibetan-mastiff', 'tibetan-terrier',
                   'treeing-walker-coonhound', 'weimaraner', 'welsh-springer-spaniel', 'west-highland-white-terrier',
                   'yorkshire-terrier', 'affenpinscher', 'basenji', 'basset-hound', 'beagle', 'black-and-tan-coonhound',
                   'bloodhound', 'bluetick-coonhound', 'borzoi', 'boxer', 'briard', 'bullmastiff', 'cairn-terrier',
                   'chow-chow', 'clumber-spaniel', 'cocker-spaniel', 'collie', 'curly-coated-retriever', 'dhole',
                   'carolina-dog', 'flat-coated-retriever', 'giant-schnauzer', 'golden-retriever', 'belgian-sheepdog',
                   'keeshond', 'australian-kelpie', 'komondor', 'kuvasz', 'alaskan-malamute', 'belgian-malinois',
                   'miniature-pinscher', 'miniature-poodle', 'miniature-schnauzer', 'otterhound', 'papillon', 'pug',
                   'redbone-coonhound', 'schipperke', 'silky-terrier', 'soft-coated-wheaten-terrier', 'poodle',
                   'standard-schnauzer', 'toy-poodle', 'toy-fox-terrier', 'vizsla', 'whippet', 'fox-terrier']

    loaded_model.eval()
    with torch.inference_mode():
        image_pred = loaded_model(transformed_image.unsqueeze(dim=0))
    custom_image_label = torch.argmax(torch.softmax(image_pred, dim=1), dim=1)
    predicted_breed = breeds_list[custom_image_label]

    return predicted_breed

def history_web_scrapping(breed):
    r = requests.get(f'https://dogtime.com/dog-breeds/{breed}')
    soup = BeautifulSoup(r.content, 'html.parser')
    try:
        s = soup.find_all("div", class_="xe-breed-card__description-field-content")
        choosen_p = s[2].find_all("p")
        history = '\n'.join(paragraph.get_text() for paragraph in choosen_p)
    except IndexError as e:
        history = ""

    return history

def info_web_scrapping(breed):
    r = requests.get(f'https://dogtime.com/dog-breeds/{breed}')
    soup = BeautifulSoup(r.content, 'html.parser')
    try:
        s = soup.find_all("div", class_="xe-breed-card__description-field-content")
        choosen_p = s[0].find_all("p")
        info = '\n'.join(paragraph.get_text() for paragraph in choosen_p)
    except IndexError as e:
        info = ""

    return info


