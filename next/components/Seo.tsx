import Head from 'next/head';

interface Props {
  pageTitle: string;
  pageDescription: string;
  pagePath: string;
  pageImg: string;
  pageImgWidth?: number;
  pageImgHeight?: number;
}

const Seo = ({
  pageTitle,
  pageDescription,
  pagePath,
  pageImg,
  pageImgWidth,
  pageImgHeight,
}: Props) => {
  const title = pageTitle;
  const description = pageDescription;
  const url = pagePath;
  const imgUrl = pageImg;
  const imgWidth = pageImgWidth ? pageImgWidth : 1024;
  const imgHeight = pageImgHeight ? pageImgHeight : 576;

  return (
    <Head>
      <title>{title}</title>
      <meta name="viewport" content="width=device-width,initial-scale=1.0" />
      <meta name="description" content={description} />
      <meta property="og:url" content={url} />
      <meta property="og:title" content={title} />
      <meta property="og:site_name" content={title} />
      <meta property="og:description" content={description} />
      <meta property="og:type" content="website" />
      <meta property="og:image" content={imgUrl} />
      <meta property="og:image:width" content={String(imgWidth)} />
      <meta property="og:image:height" content={String(imgHeight)} />

      <meta name="twitter:card" content="summary_large_image" />
      <meta name="twitter:site" content="@kusobako_de" />
      <meta name="twitter:title" content={title} />
      <meta name="twitter:description" content={description} />
      <meta name="twitter:image" content={imgUrl} />

      <link rel="canonical" href={url} />
    </Head>
  );
};

export default Seo;
