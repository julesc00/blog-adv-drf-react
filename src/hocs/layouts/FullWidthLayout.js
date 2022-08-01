import { connect } from "react-redux"

import NavBar from "components/navigation/NavBar"
import Footer from "components/navigation/Footer"

const FullWidthLayout = ({ children }) => {
    return (
        <>
            <NavBar />
            {children}
            <Footer />
        </>
    )
}

const mapStateToProps = state => ({

})

export default connect(mapStateToProps, {

})(FullWidthLayout)