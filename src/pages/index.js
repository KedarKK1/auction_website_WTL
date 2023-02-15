import Head from 'next/head'
import Image from 'next/image'
import { Inter } from '@next/font/google'
import styles from '@/styles/Home.module.css'
// import 'tw-elements';

const inter = Inter({ subsets: ['latin'] })

export default function Home() {
  return (
    <div >
      <Head>
        {/* <script src="./TW-ELEMENTS-PATH/dist/js/index.min.js"></script> */}
      </Head>
        +Hello World
    </div>
  )
}
