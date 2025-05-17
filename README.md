# 📈 Finnhub-Api-Spec
This project demonstrates the end-to-end documentation and integration workflow of a financial data API using the **Finnhub.io** OpenAPI specification. It showcases API documentation, client generation, testing, and Python scripting.
## 🗂 Project Structure
finnhub-api-spec/
finnhub-api.yaml # OpenAPI 3.0 specification (imported from Finnhub)
test_quote.py # Python script calling the live /quote endpoint
python-client/ # Auto-generated Python client SDK
README.md # Project README file

## 🧪 Running the Python Test Script
The script `test_quote.py` demonstrates a real-world use of the `/quote` endpoint via the generated client.

Before running, make sure to:

- Replace `"your_finnhub_api_key"` in `test_quote.py` with your actual Finnhub API key.
- Install required dependencies (if any).

Run the script from the command line:

```bash
python3 test_quote.py
```
You should see a live response from the Finnhub API with the stock quote data.

## ⚙️ Generating the Python Test Script
The Python client SDK was generated from the OpenAPI specification using OpenAPI Generator:

```bash
openapi-generator-cli generate \
  -i finnhub-api.yaml \
  -g python \
  -o python-client
```

## 📚 Additional Resources

- [Finnhub API Documentation](https://finnhub.io/docs/api)  
- [OpenAPI Specification](https://swagger.io/specification/)  
- [OpenAPI Generator](https://openapi-generator.tech/)

