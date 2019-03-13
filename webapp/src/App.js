import React, { Component } from 'react';

const ticketTypes = {
    0: {
        name: 'Street Cleaning',
        description: 'tbd'
    },
    1: {
        name: 'Meter Expired',
        description: 'tbd'
    },
    2: {
        name: 'Red Zone',
        description: 'tbd'
    },
    3: {
        name: 'Preferred Parking',
        description: 'tbd'
    },
    4: {
        name: 'Display of Tabs/Plate',
        description: 'tbd'
    },
    5: {
        name: 'No Parking',
        description: 'tbd'
    },
    6: {
        name: 'Parking Over Time Limit',
        description: 'tbd'
    },
    7: {
        name: 'White Zone',
        description: 'tbd'
    },
    8: {
        name: 'No Stopping/Standing',
        description: 'tbd'
    },
    9: {
        name: 'Yellow Zone',
        description: 'tbd'
    },
    10: {
        name: 'Improperly Parked',
        description: 'tbd'
    },
    11: {
        name: 'Fire Hydrant',
        description: 'tbd'
    },
    12: {
        name: 'Disabled Parking',
        description: 'tbd'
    },
    13: {
        name: 'Private Property',
        description: 'tbd'
    }
}

const ticketCount = 5

class App extends Component {

    constructor(props) {
        super(props);

        this.state = {
            form: {
                longitude: '34.05',
                latitude: '-118.24',
                month: '3.0',
                weekday: '4.0',
                hour: '14.0',
                make: '5.0',
                color: '7.0'
            },
            tickets: []
        }
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
                                        <input className="form-control" type="text" id="month" value={this.state.form.month} onChange={this.handleChange} />
                                    </div>
                                </div>
                                <div className="form-group row">
                                    <label className="col-sm-3 col-form-label" htmlFor="weekday">Weekday</label>
                                    <div className="col-sm-9">
                                        <input className="form-control" type="text" id="weekday" value={this.state.form.weekday} onChange={this.handleChange} />
                                    </div>
                                </div>
                                <div className="form-group row">
                                    <label className="col-sm-3 col-form-label" htmlFor="hour">Hour</label>
                                    <div className="col-sm-9">
                                        <input className="form-control" type="text" id="hour" value={this.state.form.hour} onChange={this.handleChange} />
                                    </div>
                                </div>
                                <div className="form-group row">
                                    <label className="col-sm-3 col-form-label" htmlFor="make">Vehicle Make</label>
                                    <div className="col-sm-9">
                                        <input className="form-control" type="text" id="make" value={this.state.form.make} onChange={this.handleChange} />
                                    </div>
                                </div>
                                <div className="form-group row">
                                    <label className="col-sm-3 col-form-label" htmlFor="color">Vehicle Color</label>
                                    <div className="col-sm-9">
                                        <input className="form-control" type="text" id="color" value={this.state.form.color} onChange={this.handleChange} />
                                    </div>
                                </div>
                                <div className="row justify-content-end">
                                    <div className="col-sm-9">
                                        <button type="submit" className="btn btn-primary">Search</button>
                                    </div>
                                </div>
                            </form>
                        </div>
                        {this.state.tickets.length > 0 &&
                        <div className="col-lg-6">
                            <h3>The Possible Tickets You May Recieve</h3>
                            <hr />
                            {this.state.tickets.map((ticket) => {
                                return (
                                    <div key={ticket[0]} className="row justify-content-end">
                                        <div className="col-sm-12"><b>{ticketTypes[ticket[0]].name}</b></div>
                                        <div className="col-sm-10">{ticketTypes[ticket[0]].description}<br /><br /></div>
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
