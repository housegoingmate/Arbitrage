from dataclasses import dataclass
from typing import List
import os
from dotenv import load_dotenv

load_dotenv()

@dataclass
class RetailerConfig:
    name: str
    base_url: str
    selectors: dict

@dataclass
class ResalePlatformConfig:
    name: str
    base_url: str
    api_key: str

class Config:
    def __init__(self):
        self.retailers = self._load_retailers()
        self.resale_platforms = self._load_resale_platforms()
        self.scraping_config = {
            'request_delay': float(os.getenv('REQUEST_DELAY', 2)),
            'max_retries': int(os.getenv('MAX_RETRIES', 3)),
            'timeout': int(os.getenv('TIMEOUT', 30))
        }

    def _load_retailers(self) -> List[RetailerConfig]:
        return [
            RetailerConfig(
                name='Up There Store',
                base_url='https://uptherestore.com.au',
                selectors={
                    'product': '.product-item',
                    'name': '.product-title',
                    'price': '.price',
                    'availability': '.stock-status'
                }
            ),
            # Add other retailers here
        ]

    def _load_resale_platforms(self) -> List[ResalePlatformConfig]:
        return [
            ResalePlatformConfig(
                name='StockX',
                base_url='https://stockx.com',
                api_key=os.getenv('STOCKX_API_KEY')
            ),
            ResalePlatformConfig(
                name='eBay AU',
                base_url='https://www.ebay.com.au',
                api_key=os.getenv('EBAY_API_KEY')
            )
        ]
