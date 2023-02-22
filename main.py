, etc

import React, { useState, useEffect } from 'react';
import { useQuery } from '@apollo/react-hooks';
import gql from 'graphql-tag';

const QUERY = gql`
  {
    sales {
      sales
      forecast
      demand
    }
  }
`;

function App() {
  const { loading, error, data } = useQuery(QUERY);
  const [searchTerm, setSearchTerm] = useState('');
  const [searchResults, setSearchResults] = useState([]);

  useEffect(() => {
    if (data) {
      const results = data.sales.filter(sale =>
        sale.sales.toLowerCase().includes(searchTerm)
      );
      setSearchResults(results);
    }
  }, [data, searchTerm]);

  if (loading) return <p>Loading...</p>;
  if (error) return <p>Error :(</p>;

  return (
    <div>
      <input
        type="text"
        value={searchTerm}
        onChange={e => setSearchTerm(e.target.value)}
      />
      <ul>
        {searchResults.map(result => (
          <li key={result.sales}>
            {result.sales} | {result.forecast} | {result.demand}
          </li>
        ))}
      </ul>
    </div>
  );
}

export default App;