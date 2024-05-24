import TopTeams from "../Procedures/TopTeams";
import classFind from "../Procedures/classFind";
import orderValue from "../Procedures/orderValue";
import query1 from "../Procedures/query1";
import searchId from "../Procedures/searchId";
import searchValue from "../Procedures/searchValue";

const Sections = [

    {
        id: "top-teams",
        label: "Top Teams",
        content: <TopTeams/>
    },

    {
        id: "top-scorers",
        label: "Top Scorers",
        content: <h1>Top Scorers - Work in progresss</h1>
    },
    {
        id: "class-find",
        label: "Class Find",
        content: <classFind/>
    },
    {
        id: "order-value",
        label: "Order value",
        content: <orderValue/>
    },
    {
        id: "query-1",
        label: "query",
        content: <query1/>
    },
    {
        id: "search-id",
        label: "Class Find",
        content: <searchId/>
    },
    {
        id: "class-find",
        label: "Class Find",
        content: <searchValue/>
    }
];

export default Sections;