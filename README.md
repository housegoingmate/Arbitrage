# ArbitrageScout

ArbitrageScout is an automated system for identifying profitable sneaker arbitrage opportunities in the Australian market.

## Features

- **Retail Data Collection**: Scrapes product, pricing, and stock availability from major Australian sneaker retailers
- **Resale Market Analysis**: Tracks sales data from platforms like StockX and eBay AU
- **Profit Margin Calculation**: Identifies opportunities with profit margins exceeding 15%
- **Real-Time Alerts**: Notifies users of high-priority opportunities via email/SMS
- **Customizable Filters**: Allows users to filter by brand, size, and profit thresholds

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/ArbitrageScout.git
   cd ArbitrageScout
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Configure environment variables:
   - Copy `.env.example` to `.env`
   - Update with your API keys and credentials

4. Run the application:
   ```bash
   python main.py
   ```

## Configuration

Edit `config.py` to:
- Add/remove retailers
- Configure scraping selectors
- Set profit margin thresholds

## Contributing

1. Fork the repository
2. Create a feature branch
3. Submit a pull request

## License

MIT License
