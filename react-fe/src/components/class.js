import { Component } from "react";

class Message extends Component {
    constructor() {
        super();
        this.state = {
            counter: 0,
        };
    }

    increment() {
        this.setState({
            counter: this.state.counter + 1,
        })
    }

    render(){
        return (<div>
            <h1>Component from class ! {this.props.arg1} and now state: {this.state.counter}</h1>
                <button onClick={() => this.increment()}>Click</button>
                </div>)
    }
}

export default Message;