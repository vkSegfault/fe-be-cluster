import { useState } from 'react'
import axios from "axios";
import logo from './logo.svg';
import './App.css';

import Hello2 from './components/test';
import Message from './components/message';

function App() {

   // new line start
  const [profileData, setProfileData] = useState(null)

  function getData() {
    axios({
      method: "GET",
      //url:"http://svc-be:5000/members/",   // 'svc-be' is a name of a service attached to deployment but it's inside cluster and we need to access API from outside
      //url:"http://192.168.49.2/members/",   //port is not needed because it's accessed through Ingress so by default 80 
      url:"https://app.pl/members/",   // if we are using ssl termination then we can't use IP no longer (ip adress is not terminated) but need to use DNS instead (which is terminated by ingress)
    })
    .then((response) => {
      const res = response.data;
      console.log(res);
      setProfileData(({
        profile_name: res.members,
        about_me: res.about}))
    }).catch((error) => {
      if (error.response) {
        console.log(error.response)
        console.log(error.response.status)
        console.log(error.response.headers)
        }
    })}
    //end of new line 

  return (
    <div className="App">
      <Hello2></Hello2>
      <Message/>
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <p>
          Edit <code>src/App.js</code> and save to reload.
        </p>
        <a
          className="App-link"
          href="https://reactjs.org"
          target="_blank"
          rel="noopener noreferrer"
        >
          Learn React
        </a>

        {/* new line start*/}
        <p>To get your profile details: </p><button onClick={getData}>Click me</button>
        {profileData && <div>
              <p>Profile name: {profileData.profile_name}</p>
              <p>About me: {profileData.about_me}</p>
            </div>
        }
         {/* end of new line */}
      </header>
    </div>
  );
}

export default App;

