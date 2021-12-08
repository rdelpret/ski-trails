import React, { Component } from 'react';
import Table from './components/trailsTable.js';
import Container from "@material-ui/core/Container";
import Typography from "@material-ui/core/Typography";
import CssBaseline from '@mui/material/CssBaseline';


class App extends Component {

  constructor(props) {
    super(props);
     this.state = {
      trails: []
    }
  }


  componentDidMount() {
    fetch('http://127.0.0.1:5000/')
    .then(res => res.json())
    .then(json => json.trails)
    .then(trails => this.setState({ 'trails': trails }))
  }

  render() {
    return (
       <CssBaseline>
      <div className="App">
        <Container> 
          <Typography variant="h2" align="center">
          Ski Trails
        </Typography>
          <Table trails={ this.state.trails } />
        </Container>
      </div>
      </CssBaseline>
    );
  }
}

export default App;
