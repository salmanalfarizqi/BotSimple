import React from 'react'
import Image from 'next/image'
import Link from 'next/link'

export default function Nav() {
  return (
    <div>
        <nav className=' w-full'>
            <div className='bg-white h-20 flex'>
                <div className='py-2 px-10'>
                    <Image src="/image/dbbf5c60f5b5c770184cac51c59767e8.png" width={60} height={60}/>
                </div>
                <div className='grid content-center'>
                    <p className='text-black text-2xl font-bold'>SMK 17 Agustus 1945 Surabaya</p>
                </div>
            </div>
            <div className='bg-[#EB0016] h-10 flex justify-center py-2'>
                <Link className='mx-10' href='#'>Beranda</Link>
                <Link className='mx-10' href='#'>Profil</Link>
                <Link className='mx-10' href='#'>PPDB 2024</Link>
                <Link className='mx-10' href='#'>Aplikasi Sistem</Link>
            </div>
        </nav>
    </div>
  )
}
