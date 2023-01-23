function Hello(props) {
    console.log(props)
    return (
    <h1>
        Hello there klakiers! {props.msg} {props.arg2}
        {props.children}
    </h1>
    )
}

const Hello2 = () => <h1>Hello there 2 !</h1>

export default Hello;
//export default Hello2;