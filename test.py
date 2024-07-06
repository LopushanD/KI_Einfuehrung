from Praktikum_4.NNetwork import *
import os
from PIL import Image

TestData = pd.read_csv("D:/downloads/P4_Dataset/MyOwnImages.csv",header=None)
# TestData = pd.read_csv("D:/downloads/P4_Dataset/mnist_test_full.csv",header=None)
TestTargetsRaw = TestData.iloc[:,0].values
TestInputsRaw = TestData.iloc[:,1:].values
print(TestData)
TestInputs = normalizeInputs(TestInputsRaw)
TestTargets = oneHotEncode(TestTargetsRaw,10)

network = loadNetworkFromFile()

results = network.recognize(TestInputs)
totalRecognitions = len(TestInputs)

whatPredicted = np.argmax(results,axis=1) # returns index of max value from each example in ndarray
whatCorrect = np.argmax(TestTargets,axis=1) # returns index of max value from each example in ndarray
print(f"{whatPredicted}"+'\n'+f"{whatCorrect}")
correctRecognitions = np.sum((whatPredicted == whatCorrect)) #compare indexes and sum up matches
accuracyPercentage = correctRecognitions/totalRecognitions*100
print(f" The accuracy of prediction is {accuracyPercentage}%")

# print(TestInputs)
# print(whatPredicted)

# CODE TO CONVERT OWN IMAGES TO CSV FILE

def image_to_flat_array(image_path,size=(28,28)):
    """Converts an image to a flattened array of pixel values."""
    image = Image.open(image_path).convert('L')  # Convert to grayscale
    image = image.resize(size,Image.LANCZOS)
    image_array = np.array(image)
    flat_array = image_array.flatten()
    return flat_array

def images_to_csv(image_folder, csv_filename):
    """Converts all images in a folder to a CSV file with flattened pixel arrays."""
    # List to hold all flattened image arrays
    image_data = []

    # Iterate over all files in the image folder
    for filename in os.listdir(image_folder):
        
        if filename.endswith('.png'):
            image_path = os.path.join(image_folder, filename)
            flat_array = image_to_flat_array(image_path)
            np.insert(flat_array,0,filename[0])
            image_data.append(flat_array)

    # Convert list to DataFrame
    image_df = pd.DataFrame(image_data)
    

    # Save DataFrame to CSV
    return image_df.to_csv(csv_filename, index=False, header=False)

# # # Example usage
# image_folder = "D:/downloads/P4_Dataset"  # Replace with the path to your folder containing PNG images
# csv_filename = 'D:/downloads/P4_Dataset/MyOwnImages.csv'  # Output CSV file name
# print(images_to_csv(image_folder, csv_filename))


