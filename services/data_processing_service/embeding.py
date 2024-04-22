from imgbeddings import imgbeddings
from PIL import Image

class EmbedImage():
    def __init__(self) -> None:
        self.embed_model = imgbeddings(model_path="./patch32_v1.onnx")
        print("model is loaded")
        
        
    # # loading the `imgbeddings`
    def embedd_image(self, cropped_image):
        cropped_image= Image.fromarray(cropped_image)

        # calculating the embeddings
        embedding = self.embed_model.to_embeddings(cropped_image)
        return embedding