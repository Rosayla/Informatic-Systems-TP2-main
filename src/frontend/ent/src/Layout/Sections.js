import Flights from "../Tables/flights";
import Classes from "../Tables/classes";
import Airlines from "../Tables/airlines";
import Routes from "../Tables/routes";
import Times from "../Tables/times";
const Sections = [

    {
        id: "flights",
        label: "Flights",
        content: <Flights/>
    },

    {
        id: "airlines",
        label: "Airlines",
        content: <Airlines/>
    },

    {
        id: "classes",
        label: "Classes",
        content:<Classes/>
    },
    {
        id: "routes",
        label: "Routes",
        content: <Routes/>
    },
    {
        id: "times",
        label: "Times",
        content: <Times/>
    }
];
export default Sections;