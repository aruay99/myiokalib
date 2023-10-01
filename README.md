# MyIokaLib
MyIokaLib is a Python library for interacting with the Ioka API. It provides an easy-to-use interface for creating orders, processing payments, managing customers, cards, webhooks, and more.
## Installation

```markdown
pip install git+https://github.com/aruay99/myiokalib.git
```


## Usage

```python
import myiokalib

# Initialize the API key
myiokalib.init("your_api_key")

# Create an order
order_data = {
    # Order data here
}
order = myiokalib.IokaAPI().create_order(order_data)

# Get an order by ID
order_id = "ord_123"
order = myiokalib.IokaAPI().get_order(order_id)

# More examples here
```

## Documentation

You can find the full documentation for MyIokaLib [here](DOCUMENTATION.md). It includes detailed information on how to use the library, available classes, methods, and examples.

## Contributing

Contributions are welcome! If you'd like to contribute to MyIokaLib, please follow these steps:

1. Fork the repository.
2. Create a new branch for your feature: `git checkout -b feature-name`
3. Make your changes and commit them: `git commit -m "Add feature"`
4. Push your changes to your fork: `git push origin feature-name`
5. Open a pull request to the main repository.

## License

This library is released under the MIT License. See the [LICENSE](LICENSE) file for details.
