import '@/styles/globals.css'
import { useEffect } from 'react';

export default function App({ Component, pageProps }) {
  // return <Component {...pageProps} /> // changed this to enable tailwind css and tailwind element
  useEffect(() => {
    const use = async () => {
      (await import('tw-elements')).default;
    };
    use();
  }, []);

  return <Component {...pageProps} />;
}
