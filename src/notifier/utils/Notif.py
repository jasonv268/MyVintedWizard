import json
import discord


class Notif:

    def __init__(self, username, price, likes, size, brand, title, img_link, link, scrap_date):
        self.username = username
        self.price = price
        self.likes = likes
        self.size = size
        self.brand = brand
        self.title = title
        self.img_link = img_link
        self.link = link
        self.scrap_date = scrap_date

    @classmethod
    def deserialize(cls, attributes_dict):
        return cls(**attributes_dict)

    def serialize(self):
        return json.dumps(self.__dict__)

    def get_embed(self):
        embed = discord.Embed(
            title=f"Titre: {self.title}",
            url=self.link,
            color=discord.Color.blurple()  # Couleur du message (vous pouvez changer cela selon vos besoins)
        )

        # Ajouter des champs, des images, des liens, etc., à l'objet Embed si nécessaire
        embed.add_field(name="Date", value=f"{self.scrap_date}", inline=True)
        embed.add_field(name="Marque", value=f"{self.brand}", inline=True)
        embed.add_field(name="Taille", value=f"{self.size}", inline=True)
        embed.add_field(name="User", value=f"{self.username}", inline=True)
        embed.add_field(name="Likes", value=f"{self.likes}", inline=True)
        embed.add_field(name="Price", value=f"{self.price} | {str(round(int(self.price) * 1.05 + 0.7, 2))}",
                        inline=True)

        embed.set_image(url=self.img_link)
        return embed
