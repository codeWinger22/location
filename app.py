# from flask import Flask, render_template, request, jsonify
# import time

# app = Flask(__name__)

# @app.route('/')
# def index():
#     return render_template('index.html')

# @app.route('/get_location', methods=['POST'])
# def get_location():
#     data = request.json
#     latitude = data.get('latitude')
#     longitude = data.get('longitude')

#     if latitude and longitude:
#         timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
#         location_data = f"{timestamp} - Latitude: {latitude}, Longitude: {longitude}\n"

#         with open("live_location.txt", "a") as file:
#             file.write(location_data)

#         return jsonify({'message': 'Location saved!', 'latitude': latitude, 'longitude': longitude})
#     else:
#         return jsonify({'error': 'Failed to get location'}), 400

# if __name__ == '__main__':
#     app.run(debug=True)


# from flask import Flask, render_template, request, jsonify
# import time
# import requests

# app = Flask(__name__)

# @app.route('/')
# def index():
#     return render_template('index.html')

# @app.route('/get_location', methods=['POST'])
# def get_location():
#     data = request.json
#     latitude = data.get('latitude')
#     longitude = data.get('longitude')

#     # If GPS is off, use IP-based location
#     if not latitude or not longitude:
#         ip_info = requests.get("http://ip-api.com/json/").json()
#         latitude = ip_info.get('lat')
#         longitude = ip_info.get('lon')

#     if latitude and longitude:
#         timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
#         location_data = f"{timestamp} - Latitude: {latitude}, Longitude: {longitude}\n"

#         with open("live_location.txt", "a") as file:
#             file.write(location_data)

#         return jsonify({'message': 'Location saved!', 'latitude': latitude, 'longitude': longitude})
#     else:
#         return jsonify({'error': 'Failed to get location'}), 400

# if __name__ == '__main__':
#     app.run(debug=True)


# from flask import Flask, render_template, request, jsonify
# import time
# import requests

# app = Flask(__name__)

# @app.route('/')
# def index():
#     return render_template('index.html')

# @app.route('/get_ip_location')
# def get_ip_location():
#     """Fetch location from IP if GPS is unavailable"""
#     try:
#         ip_info = requests.get("http://ip-api.com/json/").json()
#         latitude = ip_info.get('lat')
#         longitude = ip_info.get('lon')
#         return jsonify({'latitude': latitude, 'longitude': longitude})
#     except:
#         return jsonify({'error': 'Failed to fetch IP-based location'}), 500

# @app.route('/get_location', methods=['POST'])
# def get_location():
#     """Save location data from GPS or IP"""
#     data = request.json
#     latitude = data.get('latitude')
#     longitude = data.get('longitude')

#     if latitude and longitude:
#         timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
#         location_data = f"{timestamp} - Latitude: {latitude}, Longitude: {longitude}\n"

#         with open("live_location.txt", "a") as file:
#             file.write(location_data)

#         return jsonify({'message': 'Location saved!', 'latitude': latitude, 'longitude': longitude})
#     else:
#         return jsonify({'error': 'Failed to get location'}), 400

# if __name__ == '__main__':
#     app.run(debug=True)



from flask import Flask, render_template, request, jsonify
import time
import requests

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_ip_location')
def get_ip_location():
    """Fetch location from IP if GPS is unavailable"""
    try:
        ip_info = requests.get("http://ip-api.com/json/").json()
        latitude = ip_info.get('lat')
        longitude = ip_info.get('lon')
        return jsonify({'latitude': latitude, 'longitude': longitude})
    except:
        return jsonify({'error': 'Failed to fetch IP-based location'}), 500

@app.route('/get_location', methods=['POST'])
def get_location():
    """Save location data from GPS or IP"""
    data = request.json
    latitude = data.get('latitude')
    longitude = data.get('longitude')

    if latitude and longitude:
        timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
        location_data = f"{timestamp} - Latitude: {latitude}, Longitude: {longitude}\n"

        with open("live_location.txt", "a") as file:
            file.write(location_data)

        return jsonify({'message': 'Location saved!', 'latitude': latitude, 'longitude': longitude})
    else:
        return jsonify({'error': 'Failed to get location'}), 400

if __name__ == '__main__':
    app.run(debug=True)
