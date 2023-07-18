import requests

def download_facebook_video(video_url, access_token):
    # Make a GET request to the video URL with the access token
    response = requests.get(video_url, params={'access_token': access_token})
    
    # Check if the request was successful
    if response.status_code == 200:
        # Extract the video URL from the response
        video_data = response.json()
        video_source = video_data['source']
        
        # Download the video
        response = requests.get(video_source)
        
        # Save the video to a file
        if response.status_code == 200:
            with open('video.mp4', 'wb') as f:
                f.write(response.content)
            print('Video downloaded successfully!')
        else:
            print('Failed to download video:', response.status_code)
    else:
        print('Failed to retrieve video URL:', response.status_code)


# Example usage
video_url = 'https://graph.facebook.com/v12.0/{video_id}'
access_token = 'YOUR_ACCESS_TOKEN'

download_facebook_video(video_url, access_token)
