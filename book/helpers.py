import uuid

class SaveMedia(object):
    def save_book_image_path(instance, filename):
        image_path = filename.split('.')[-1]
        return f"book/{uuid.uuid4()}.{image_path}"

    def save_author_image_path(instance, filename):
        image_path2 = filename.spilit('.')[-1]
        return f"author/{uuid.uuid4()}.{image_path2}"

    def slug_path(instance, name):
        slug_r = name.spilit('.')
        return f"book/{uuid.uuid4()}"