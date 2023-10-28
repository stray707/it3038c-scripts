window.onload=function() {
    'use strict';

    var ajax = new XMLHttpRequest();

    // The ID and secret provided by the Spotify Developer Dashboard
    var clientID = '915f4421fa2e4032ade70b0ab6380def';
    var clientSecret ='3ec4eb56ea994bceb1ed0a28544cebbd';

    var credential = btoa(clientID + ':' + clientSecret);
    var token = undefined;

    // POSTing upon window load
    $.ajax ({
        url: 'https://accounts.spotify.com/api/token',
        method: 'POST',
        dataType: 'json',
        headers: {
            'Authorization': 'Basic ' + credential,
            'Content-Type': 'application/x-www-form-urlencoded'
        },
        data: {
            'grant_type': 'client_credentials'
        },
        success: function(data) {
            console.log(data.access_token);
            // Using the token for later requests
            token = data.access_token;
        },
        error: function(jqXHR, textStatus, errorThrown) {
            console.log('Request failed. ' + textStatus)
        }
    });

    // ID search button
    $('#albumSearch').click(function() {
        getAlbumInfo();
    });

    // Name search button
    $('#albumNameSearch').click(function() {
    searchByAlbumName();
    });

    // Album Name Search click listener
    $('#albumList').on('click', 'li', function() {
        var albumID = $(this).data('album-id');
        // Insert the album ID into the #albumSubmission input field
        $('#albumSubmission').val(albumID);
        // Fetch and display the tracks of the selected album
        getAlbumInfo(albumID);
    });

    // Search by Album Name
    function searchByAlbumName() {
        var albumName = $('#albumName').val();

        // Validate the input
        if (!albumName.trim()) {
            alert('Please enter an album name');
            return;
        }

        $.ajax({
            url: 'https://api.spotify.com/v1/search',
            type: 'GET',
            data: {
                q: albumName,
                type: 'album',
                limit: 10 // limiting the results to 10 albums
            },
            headers: {
                'Authorization': 'Bearer ' + token
            },
            success: function(data) {
                // Clear the album list
                $('#albumList').empty();

                // Loop through the albums and append each one to the album list
                data.albums.items.forEach(function(album) {
                    $('#albumList').append('<li data-album-id="' + album.id + '">' + album.name + ' by ' + album.artists[0].name + '</li>');
                });
            },
            error: function(xhr, status, error) {
                console.log('HTTP Status: ' + xhr.status);
                console.log('Error message: ' + error);
            }
        });
    }

    // Asks for album tracks
    function getAlbumInfo() {

        // Spotify API returns album information upon recieving an ID
        var albumID = $('#albumSubmission').val();

            // Validate the input
            if (!albumID.trim()) {
            alert('Please enter an album ID');
            return;
        }


        console.log(albumID);

        // Clear the track list before appending new items
        $('#trackList').empty();

        $.ajax({
            url: 'https://api.spotify.com/v1/albums/' + albumID,
            type: 'GET',
            dataType: 'json',
            headers: {
                'Authorization': 'Bearer ' + token
            },
            success: function(data) {
                console.log('fetch success');
                console.log(data);

                    // Display album and artist information, using jQuery's .html() function.
                    // Sometimes there are multiple artists, but here we will just take the first name in the array
                    $('#albumInfo').html('<h2>' + data.name + '</h2>' + '<p>By ' + data.artists[0].name + '</p>');

                    // Appending DOM with tracks and embedding the track ID within each item
                    data.tracks.items.forEach(function(track) {
                    $('#trackList').append('<li data-track-id="' + track.id + '">' + track.name + '</li>');
                });
            },
            error: function(xhr, status, error) {
                console.error(error)
                console.log('HTTP Status: ' + xhr.status);
            }
        })
    }

    // Listener for clicks on track
    $('#trackList').on('click', 'li', function() {
    var trackID = $(this).data('track-id');
    getTrackAnalysis(trackID);
    });

    // Function for getting track details after list is made
    function getTrackAnalysis(trackID) {
    $.ajax({
        url: 'https://api.spotify.com/v1/audio-analysis/' + trackID,
        type: 'GET',
        dataType: 'json',
        headers: {
            'Authorization': 'Bearer ' + token
        },

        success: function(data) {
            console.log('fetch success');

            // creating a map key for the value given by the API
            var keyMapping = {
                0: 'C',
                1: 'C♯, D♭',
                2: 'D',
                3: 'D♯, E♭',
                4: 'E',
                5: 'F',
                6: 'F♯, G♭',
                7: 'G',
                8: 'G♯, A♭',
                9: 'A',
                10: 'A♯, B♭',
                11: 'B'
            };

            $('#loudness').val(data.track.loudness + ' db');
            $('#tempo').val(data.track.tempo + ' bpm');
            $('#time_signature').val(data.track.time_signature);
            $('#key').val(keyMapping[data.track.key]);
            },

        error: function(xhr, status, error) {
            console.log('HTTP Status: ' + xhr.status);
            console.log('Error message: ' + error);

            }

        });

    }

}   