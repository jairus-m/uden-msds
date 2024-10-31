class Artist:
    def __init__(self, name, art_type, favorite_piece):
        """Class constructor"""
        self.name = name
        self.art_type = art_type
        self.favorite_piece = favorite_piece
    
    def __str__(self):
        """Returns string when called in print()"""
        return f'Artist(name={self.name}, art_type={self.art_type})'
    
    def describe_artist(self):
        return f'{self.name} makes {self.art_type} art.'
    
class Musician(Artist):
    def __init__(self, name, genre, favorite_piece, art_type='musical'):
        """"""
        super().__init__(name, art_type, favorite_piece)
        self.genre = genre
    def __str__(self):
        return f'Musician(name={self.name}, art_type={self.art_type})'
    def describe_artist(self):
        return f'{self.name} makes {self.genre} music.'
    def set_favorite_piece(self, new_favorite_piece):
        self.favorite_piece = new_favorite_piece


if __name__ == '__main__':
    monet = Artist(name='Claude Monet', art_type='painted', favorite_piece='Sunrise, 1872')
    dijon = Musician(name='Dijon Duenas', genre='alternative R&B', favorite_piece='Absolutely')

    # assert statments for attributes
    assert monet.name == 'Claude Monet'
    assert monet.art_type == 'painted'
    assert monet.favorite_piece == 'Sunrise, 1872'

    # assert statement for describe_artist() method
    assert monet.describe_artist() == 'Claude Monet makes painted art.'

    # assert statement for attributes
    assert dijon.name == 'Dijon Duenas'
    assert dijon.art_type == 'musical'
    assert dijon.favorite_piece == 'Absolutely'

    # use set_favorite_piece() to override favorite_piece attribute
    dijon.set_favorite_piece('How Do You Feel About Getting Married?')
    # assert statement for favorite_piece
    assert dijon.favorite_piece == 'How Do You Feel About Getting Married?'

    # assert statement for the overidden, non-magic method describe_artist()
    assert dijon.describe_artist() == 'Dijon Duenas makes alternative R&B music.'

    print(f'{monet}\n{monet.name}\n{monet.describe_artist()}\n{monet.favorite_piece}\n{monet.art_type}')
    print('--- -- '*6)
    print(f'{dijon}\n{dijon.name}\n{dijon.describe_artist()}\n{dijon.favorite_piece}\n{dijon.art_type}')
    print('--- -- '*6)
    print('All tests passed!')
