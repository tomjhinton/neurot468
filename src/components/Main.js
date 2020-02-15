//pic size 687*687
import React from 'react'
import axios from 'axios'




class Main extends React.Component{
  constructor(){
    super()
    this.state = {
      data: {},
      error: ''

    }
    this.componentDidMount = this.componentDidMount.bind(this)





  }


  componentDidMount(){
    axios.get('/api/works')
      .then(res => this.setState({works: res.data}))
  

  }

  componentDidUpdate(){



  }




  render() {

    console.log(this.state)

    return (
      <div>

      HIYA


      </div>




    )
  }
}
export default Main
