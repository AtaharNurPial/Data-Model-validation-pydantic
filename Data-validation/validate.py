''' "Name": "Game of Thrones",
    "subtitle": "subtitle": "Pivot!!! piiiivoooooot!!!!",
    "author": "Goerge R.R Martin",
    "publisher": "HBO",
    "IMDB_Rating": "9.5",
    "Runtime": "50 Mins",
    "Episode": 68 ,
    "Cast":'''
import pydantic
from pydantic import BaseModel
import json
from pprint import pprint
from typing import List, Optional

class TVSeries(BaseModel):
    title: str
    subtitle: Optional[str]
    author: str
    publisher: str
    imdb_rating: float
    runtime: str
    episode: int
    cast: dict

    '''dont need constructor in Basemodel'''
    # def __init__(self, title,subtitle,author,publisher,imdb_rating,runtime,episode,cast) -> None:
    #     self.title = title
    #     self.subtittle = subtitle
    #     self.author = author
    #     self.publisher = publisher
    #     self.imdb_rating = imdb_rating
    #     self.runtime = runtime
    #     self.episode = episode
    #     self.cast = cast
    
def main():
    with open('data/series_data.json') as info:
        data = json.load(info)
        infos: List[TVSeries] = [TVSeries(**item) for item in data]

        pprint(infos[2])
        '''[<__main__.TVSeries object at 0x7f6815206be0>,
            <__main__.TVSeries object at 0x7f681515e9d0>,
            <__main__.TVSeries object at 0x7f6815104e50>] thats the output if we do not use pydantic.'''
if __name__ == "__main__":
    main()

    '''once we used BaseModel, the type error in imbd_rating was auto removed. It was showing float as it 
    suppose to be even though in series_data.json the type is a string.'''

