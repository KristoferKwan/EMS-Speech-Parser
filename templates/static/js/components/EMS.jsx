import React, { Component } from 'react';
import Button from 'react-bootstrap/Button';
import axios from 'axios';

export default class EMS extends Component {
   constructor(props) {
      super(props);

      this.state = {
          incident_address : '',
          incident_number : '',
          patient : {
            first_name: '',
            last_name: ''
          }, 
          incident_date: new Date(),
          allergies: '',
          incident_patient_disposition: {
            treated_transport_ems: false,
            canceled: false,
            no_treatment_required: false,
            treated_and_released: false,
            no_patient_found: false,
            no_treatment_required: false,
            dead_at_scene: false,   
          }
      }

  }
   
  componentDidMount(){
      this.setState({
         allergies : "test allergy" 
      })   
   }
   
   parseInfo(e){
      axios.get('http://localhost:5000/parse_ems_info/')
         .then(response => {
            if(response.data.length > 0){
               this.setState({
                  
               })
            }
         })
      this.setState({ //this needs to refer to the class
          username: e.target.value
      })    
  }
   


   render() {
       return (
         <div className = "voice-recording" >
            <Button onClick = {parseInfo} >Voice recording</Button>
         </div>   
       )
    }
}