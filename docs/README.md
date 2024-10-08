# Mini-OTA-Test

## Project Overview
**Mini-OTA-Test** is a simple project that demonstrates Over-the-Air (OTA) updates for a virtual vehicle controller. It includes a basic OTA server for distributing updates, a simulated vehicle client to download and install updates, and automated tests to validate the success of the update process.

The goal is to simulate and test the OTA update process in a controlled environment using Flask for the server and `pytest` for testing.

## Project Structure

```
Mini-OTA-Test/
│
├── src/
│   ├── ota_server.py      # Flask server that serves OTA updates
│   ├── ota_client.py      # Client script simulating a vehicle downloading updates
│   ├── test_ota.py        # Test cases for the OTA process
│
├── updates/
│   └── update_v1.1.bin    # The update file to be downloaded by the client
│
└── README.md              # Project documentation
```

## Requirements

- Python 3.10+
- Flask
- Requests library
- Pytest (for running tests)

### Install dependencies
You can install the required dependencies with the following command:

```bash
pip install Flask requests pytest
```

## How to Run the Project

1. **Start the OTA Server**:
   Navigate to the `src/` folder and start the server:

   ```bash
   python ota_server.py
   ```

   The server will be running on `http://localhost:5000`.

2. **Run the Client**:
   In a separate terminal, you can run the OTA client to simulate a vehicle downloading the update:

   ```bash
   python ../src/ota_client.py
   ```

   If the server is running and the update file is available, the client will download and install the update.

## Running the Tests

To run the automated tests using `pytest`, execute the following command in the `src/` directory:

```bash
pytest ../src/test_ota.py
```

You should see output indicating that the tests passed successfully:

```
===================================== test session starts =====================================
platform linux -- Python 3.10.x
collected 2 items

test_ota.py ..                                                                   [100%]

===================================== 2 passed in 0.04s =======================================
```

## Features

- **OTA Server**: A simple Flask server serving OTA update files.
- **OTA Client**: A basic client simulating the download and installation of an update.
- **Automated Tests**: Pytest-based tests to validate the OTA process.

## Future Enhancements

- Simulate network interruptions during the update.
- Add integrity checks for the downloaded file.
- Integrate with a vehicle simulation framework like CARLA or Gazebo for more realistic testing.

## License

This project is open-source and available under the MIT License.
