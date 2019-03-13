import React, { Component } from 'react';
import {Map, GoogleApiWrapper} from 'google-maps-react';

export class MapContainer extends Component {

    render() {
        return (
            <Map google={this.props.google} zoom={9}>
            </Map>
        );
    }

}

export default GoogleApiWrapper({
    apiKey: 'AIzaSyCgyB-8lqWqGhTYSlt2VuJyeuEVotFoYO8'
})(MapContainer)
