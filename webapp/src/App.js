/*
Copyright 2019, John Hoff <john.hoff@braindonor.net>
Creative Commons Attribution-ShareAlike 4.0 International License
*/

import React, { Component } from 'react';
import GoogleMapReact from 'google-map-react';

import { Hours, Months, TicketTypes, VehicleMakes, VehilceColors, Weekdays } from './Constants';

const ticketCount = 4

class App extends Component {

    static defaultProps = {
        center: {
            lat: '34.05',
            lng: '-118.24' 
        },
        zoom: 9
    }

    constructor(props) {
        super(props);

        this.state = {
            form: {
                latitude: '34.05',
                longitude: '-118.24',
                month: '3.0',
                weekday: '4.0',
                hour: '14.0',
                make: '5.0',
                color: '7.0'
            },
            tickets: []
        }
    }

    handleMapClick = ({x, y, lat, lng, event}) => {
        let newForm = this.state.form;
        newForm.latitude = lat;
        newForm.longitude = lng;
        this.setState({form: newForm});
    }

    handleChange = (event) => {
        let newForm = this.state.form;
        newForm[event.target.id] = event.target.value;
        this.setState({form: newForm});
    }

    handleSubmit = (event) => {
        event.preventDefault();

        fetch('/ticketPrediction', {
            method: 'POST',
            headers: {
                'Accept': 'application/json',
                'Content-Type': 'application/json'
            },
            body: JSON.stringify([this.state.form])
        })
        .then((response) => response.json())
        .then((responseJson) => {
            let ticketPredictions = []
            for (let i = 0; i < responseJson.length; i++) {
                ticketPredictions.push([i, responseJson[i]])
            }
            ticketPredictions.sort(function(first, second) {
                return second[1] - first[1];
            });
            this.setState({ tickets: ticketPredictions.slice(0, ticketCount)});
        })
        .catch((error) => {
            console.error(error);
        })
    }

    render() {
        return (
            <div>
                <nav className="navbar navbar-expand-lg navbar-dark bg-dark static-top">
                    <div className="container">
                        <span className="navbar-brand">LA Parking Ticket Application</span>
                        <ul className="navbar-nav ml-auto">
                            <li className="nav-item active">
                                <a className="nav-link" href="https://github.com/theBraindonor/la-parking-tickets" target="_blank" rel="noopener noreferrer">View On Github</a>
                            </li>
                        </ul>
                    </div>
                </nav>
                <br /><br />
                <div className="container">
                    <div className="row">
                        <div className="col-lg-6">
                            <div style={{height: '430px', width: '540px'}}>
                                <GoogleMapReact
                                    bootstrapURLKeys={{key: 'AIzaSyCgyB-8lqWqGhTYSlt2VuJyeuEVotFoYO8'}}
                                    defaultCenter={{lat: 34.05, lng: -118.24}}
                                    defaultZoom={10}
                                    onClick={this.handleMapClick}
                                >
                                <div
                                    lat={this.state.form.latitude}
                                    lng={this.state.form.longitude}
                                    className="mapMarker"
                                ></div>
                                </GoogleMapReact>
                            </div>
                            <br />
                            <form onSubmit={this.handleSubmit}>
                                <div className="form-group row">
                                    <label className="col-sm-3 col-form-label" htmlFor="latitude">Latitude</label>
                                    <div className="col-sm-9">
                                        <input className="form-control" type="text" id="latitude" value={this.state.form.latitude} onChange={this.handleChange} />
                                    </div>
                                </div>
                                <div className="form-group row">
                                    <label className="col-sm-3 col-form-label" htmlFor="longitude">Longitude</label>
                                    <div className="col-sm-9">
                                        <input className="form-control" type="text" id="longitude" value={this.state.form.longitude} onChange={this.handleChange} />
                                    </div>
                                </div>
                                <div className="form-group row">
                                    <label className="col-sm-3 col-form-label" htmlFor="month">Month</label>
                                    <div className="col-sm-9">
                                        <select className="form-control" id="month" value={this.state.form.month} onChange={this.handleChange}>
                                            {Months.map((month) => {
                                                return (
                                                    <option key={month.value} value={month.value}>{month.label}</option>
                                                )
                                            })}
                                        </select>
                                    </div>
                                </div>
                                <div className="form-group row">
                                    <label className="col-sm-3 col-form-label" htmlFor="weekday">Weekday</label>
                                    <div className="col-sm-9">
                                        <select className="form-control" id="weekday" value={this.state.form.weekday} onChange={this.handleChange}>
                                            {Weekdays.map((weekday) => {
                                                return (
                                                    <option key={weekday.value} value={weekday.value}>{weekday.label}</option>
                                                )
                                            })}
                                        </select>
                                    </div>
                                </div>
                                <div className="form-group row">
                                    <label className="col-sm-3 col-form-label" htmlFor="hour">Hour</label>
                                    <div className="col-sm-9">
                                        <select className="form-control" id="hour" value={this.state.form.hour} onChange={this.handleChange}>
                                            {Hours.map((hour) => {
                                                return (
                                                    <option key={hour.value} value={hour.value}>{hour.label}</option>
                                                )
                                            })}
                                        </select>
                                    </div>
                                </div>
                                <div className="form-group row">
                                    <label className="col-sm-3 col-form-label" htmlFor="make">Vehicle Make</label>
                                    <div className="col-sm-9">
                                        <select className="form-control" id="make" value={this.state.form.make} onChange={this.handleChange}>
                                            {VehicleMakes.map((make) => {
                                                return (
                                                    <option key={make.value} value={make.value}>{make.label}</option>
                                                )
                                            })}
                                        </select>
                                    </div>
                                </div>
                                <div className="form-group row">
                                    <label className="col-sm-3 col-form-label" htmlFor="color">Vehicle Color</label>
                                    <div className="col-sm-9">
                                        <select className="form-control" id="color" value={this.state.form.color} onChange={this.handleChange}>
                                            {VehilceColors.map((color) => {
                                                return (
                                                    <option key={color.value} value={color.value}>{color.label}</option>
                                                )
                                            })}
                                        </select>
                                    </div>
                                </div>
                                <div className="row justify-content-end">
                                    <div className="col-sm-9">
                                        <button type="submit" className="btn btn-primary">Search</button>
                                    </div>
                                </div>
                            </form>
                            <br />
                        </div>
                        {this.state.tickets.length > 0 &&
                        <div className="col-lg-6">
                            <h3>The Possible Tickets You May Recieve</h3>
                            <hr />
                            {this.state.tickets.map((ticket) => {
                                return (
                                    <div key={ticket[0]} className="row justify-content-end">
                                        <div className="col-sm-12"><b>{TicketTypes[ticket[0]].name}</b></div>
                                        <div className="col-sm-10">{TicketTypes[ticket[0]].description}<br /><br /></div>
                                    </div>
                                )
                            })}
                        </div>
                        }
                    </div>
                </div>
            </div>
        );
    }
}

export default App;
